#!/usr/bin/env python3
"""
generate_presentation.py

Builds an HTML practice-question presentation (in the style of the
original lecture4notes.html) out of a set of Python solution files named
q1_sol.py, q2_sol.py, q3_sol.py, ... in a folder.

Each qN_sol.py file must start with a module docstring (a triple-quoted
string as the very first thing in the file, after any comments) containing
the question text written in Markdown. Everything in the file *after* that
docstring is treated as the sample solution code and shown verbatim.

Example q1_sol.py:

    \"\"\"
    Write a program that reads a phrase from the user and prints it
    sandwiched between two lines of dash characters.
    \"\"\"

    phrase = input('Enter a phrase: ')
    line = '-' * len(phrase)
    print(line)
    print(phrase)
    print(line)

Usage:
    python3 generate_presentation.py
    python3 generate_presentation.py -d /path/to/lecture -o lecture5.html -t "Lecture 5 Practice"

By default it looks for qN_sol.py files in the same folder this script
lives in, and writes presentation.html into that same folder. The HTML
template for the page's styling and behaviour is built into this script
(TEMPLATE_HTML, near the bottom), so this one file is all you need.

For each qN_sol.py it also writes a companion qN.py stub file: the same
leading comments and docstring (i.e. the question), but with the solution
code removed -- handy for handing out to students. It also writes a
README.md in the same folder, titled "<folder name> Questions and Answers",
with a list linking to each qN.py stub and, in brackets, its qN_sol.py
solution file, plus links to the two PDFs described below.

Finally, it writes two PDFs of all the questions, each question on a new
page under a clear "Question N" heading:
    <folder name>_questions.pdf               -- questions only, titled
                                                 "<folder name> Practice Questions"
    <folder name>_questions_and_solutions.pdf -- each question followed by its
                                                 sample solution, titled "<folder
                                                 name> Practice Questions and
                                                 Solutions"
They're written directly by this script -- no browser or extra libraries
needed.

To make a new presentation:
    1. Write q1_sol.py, q2_sol.py, q3_sol.py, ... in a folder, each with a
       docstring (the question, in Markdown) followed by the solution code.
    2. Run this script (optionally with -o to name the output file).
    3. Open the generated HTML file in a browser.

To update a presentation after changing a question or its solution, just
edit its qN_sol.py file and re-run this script -- it overwrites the output
file, the qN.py stub files, README.md, and the PDFs.

Note: qN.py, README.md, and the PDFs are generated files, derived from
qN_sol.py -- re-running this script overwrites them, so don't hand-edit them.
"""
import argparse
import ast
import html
import os
import re
import sys
import zlib
from pathlib import Path

QFILE_PATTERN = re.compile(r'^q(\d+)_sol\.py$', re.IGNORECASE)
MARKER = '<!-- QUESTION_BLOCKS -->'


HELP_TEXT = """\
how to use it:
  1. Put this program in a folder.

  2. In that same folder, write one file per question, named
     q1_sol.py, q2_sol.py, q3_sol.py, and so on.

  3. Start each file with the question inside triple quotes (Markdown is
     allowed), then put the sample solution code underneath. For example:

         \"\"\"
         Write a program that asks for your name and says hello.
         \"\"\"

         name = input('What is your name? ')
         print('Hello,', name)

  4. Run the program:

         python3 generate_presentation.py

  5. Open presentation.html in a web browser.

what it creates (and overwrites every time you run it):
  presentation.html                     the presentation
  q1.py, q2.py, ...                     question-only files for students
  README.md                             links to all the files
  <folder>_questions.pdf                all the questions
  <folder>_questions_and_solutions.pdf  all the questions with solutions

To change a question, edit its qN_sol.py file and run the program again.
Don't edit the generated files by hand -- your changes would be lost.

examples:
  python3 generate_presentation.py
  python3 generate_presentation.py -t "Lecture 11 Practice"
  python3 generate_presentation.py -d ../lecture12 -o lecture12.html
"""


def find_question_files(directory: Path):
    """Return [(number, path), ...] for every qN_sol.py file in directory, sorted by N."""
    found = []
    for p in directory.iterdir():
        if p.is_file():
            m = QFILE_PATTERN.match(p.name)
            if m:
                found.append((int(m.group(1)), p))
    found.sort(key=lambda t: t[0])
    return found


def parse_solution_file(path: Path):
    """Split a qN_sol.py file into (header_source, question_markdown, solution_code).

    The question is the file's module docstring (must be the first
    statement in the file, ignoring comments). header_source is everything
    from the start of the file through the end of that docstring (i.e. any
    leading comments plus the docstring itself), used to build the qN.py
    stub. solution_code is everything in the file after the docstring,
    taken verbatim.
    """
    source = path.read_text(encoding='utf-8')
    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError as e:
        sys.exit(f"Error: {path.name} has a syntax error and can't be parsed: {e}")

    docstring = ast.get_docstring(tree, clean=True)
    if docstring is None or not tree.body:
        sys.exit(
            f"Error: {path.name} has no module docstring. Add a triple-quoted "
            f"string at the very top of the file (before any code) with the "
            f"question text in Markdown."
        )

    docstring_node = tree.body[0]
    lines = source.splitlines()
    header_source = '\n'.join(lines[:docstring_node.end_lineno]).rstrip('\n') + '\n'
    solution_code = '\n'.join(lines[docstring_node.end_lineno:]).strip()

    if not solution_code:
        sys.exit(
            f"Error: {path.name} has no code after its docstring. Add the "
            f"sample solution below the triple-quoted question text."
        )

    return header_source, docstring.strip(), solution_code


def build_qfile_block(number: int, path: Path, question_md: str, solution_code: str) -> str:
    if '</script' in question_md.lower() or '</script' in solution_code.lower():
        print(
            f"Warning: {path.name} contains the text '</script', which would break "
            f"the generated HTML. Please rename or rephrase that part of the file.",
            file=sys.stderr,
        )
    combined = (
        "## Question\n\n"
        f"{question_md}\n\n"
        "## Sample Solution\n\n"
        "```python\n"
        f"{solution_code}\n"
        "```"
    )
    qid = f"q{number}"
    label = f"Q{number}"
    return (
        f'<script type="text/plain" class="qfile" data-id="{qid}" '
        f'data-file="{html.escape(path.name)}" data-label="{html.escape(label)}">\n'
        f'{combined}\n'
        f'</script>'
    )


def rename_self_reference_comment(header_source: str, old_name: str, new_name: str) -> str:
    """If a whole comment line is just the old filename (e.g. "# q1_sol.py"),
    rewrite it to name the new file instead (e.g. "# q1.py"). Leaves every
    other line -- including comments that mention the filename alongside
    other text -- untouched.
    """
    pattern = re.compile(r'^(\s*#\s*)' + re.escape(old_name) + r'\s*$')
    lines = header_source.split('\n')
    renamed = []
    for line in lines:
        m = pattern.match(line)
        renamed.append(f'{m.group(1)}{new_name}' if m else line)
    return '\n'.join(renamed)


def write_stub_files(parsed, directory: Path):
    """Write qN.py for each parsed question (header/docstring, no solution code)."""
    written = []
    for number, sol_path, header_source, _question_md, _solution_code in parsed:
        stub_name = f"q{number}.py"
        stub_path = directory / stub_name
        stub_source = rename_self_reference_comment(header_source, sol_path.name, stub_name)
        stub_path.write_text(stub_source, encoding='utf-8')
        written.append(stub_path)
    return written


def write_readme(parsed, directory: Path, questions_pdf: Path, solutions_pdf: Path):
    """Write README.md with a list linking each qN.py to its qN_sol.py,
    followed by links to the two PDFs of all the questions."""
    lines = [f"# {directory.name} Questions and Answers", ""]
    for number, sol_path, _header_source, _question_md, _solution_code in parsed:
        stub_name = f"q{number}.py"
        sol_name = sol_path.name
        lines.append(f"- [{stub_name}]({stub_name}) ([{sol_name}]({sol_name}))")
    # link relative to the README (as_posix() keeps forward slashes for Markdown)
    q_link = Path(os.path.relpath(questions_pdf, directory)).as_posix()
    s_link = Path(os.path.relpath(solutions_pdf, directory)).as_posix()
    lines.append("")
    lines.append("All the questions in one file:")
    lines.append("")
    lines.append(f"- Questions only: [{q_link}]({q_link})")
    lines.append(f"- Questions and solutions: [{s_link}]({s_link})")
    lines.append("")
    readme_path = directory / "README.md"
    readme_path.write_text('\n'.join(lines), encoding='utf-8')
    return readme_path


# ---------------------------------------------------------------------------
# PDF of all the questions and solutions, written directly with plain Python
# ---------------------------------------------------------------------------
# No extra libraries or browser needed: this writes a simple PDF by hand,
# using the three fonts every PDF reader has built in (Helvetica,
# Helvetica-Bold, and Courier). It understands the same small Markdown
# subset the presentation does: paragraphs, "- " bullet lists, ``` code
# fences, `code`, **bold**, and $math$ (shown as plain text).

# Character widths (per 1000 units of font size) for ASCII 32..126.
_HELVETICA_WIDTHS = [
    278, 278, 355, 556, 556, 889, 667, 191, 333, 333, 389, 584, 278, 333, 278, 278,
    556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 278, 278, 584, 584, 584, 556,
    1015, 667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722, 778,
    667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 278, 278, 278, 469, 556,
    333, 556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222, 833, 556, 556,
    556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500, 334, 260, 334, 584,
]
_HELVETICA_BOLD_WIDTHS = [
    278, 333, 474, 556, 556, 889, 722, 238, 333, 333, 389, 584, 278, 333, 278, 278,
    556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 333, 333, 584, 584, 584, 611,
    975, 722, 722, 722, 722, 667, 611, 778, 722, 278, 556, 722, 611, 833, 722, 778,
    667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 333, 278, 333, 584, 556,
    333, 556, 611, 556, 611, 556, 333, 611, 611, 278, 278, 556, 278, 889, 611, 611,
    611, 611, 389, 556, 333, 611, 556, 778, 556, 556, 500, 389, 280, 389, 584,
]
# PDF resource names for the three fonts
_FONTS = {'regular': ('F1', 'Helvetica'), 'bold': ('F2', 'Helvetica-Bold'),
          'mono': ('F3', 'Courier')}

PAGE_W, PAGE_H = 612, 792        # US Letter, in points (72 points = 1 inch)
MARGIN = 60
TEXT_W = PAGE_W - 2 * MARGIN
BODY_SIZE, BODY_LEADING = 11, 15
CODE_SIZE, CODE_LEADING = 9.5, 12
CODE_PAD = 8                     # space between a code box's edge and its text


def _text_width(text: str, style: str, size: float) -> float:
    if style == 'mono':
        return len(text) * 0.6 * size
    table = _HELVETICA_BOLD_WIDTHS if style == 'bold' else _HELVETICA_WIDTHS
    total = sum(table[ord(c) - 32] if 32 <= ord(c) <= 126 else 556 for c in text)
    return total * size / 1000


def _pdf_string(text: str) -> str:
    """Encode text as a PDF string literal (Windows-1252, which the built-in
    fonts use); characters that can't be encoded become '?'."""
    raw = text.encode('cp1252', errors='replace').decode('latin-1')
    return '(' + raw.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)') + ')'


def _inline_runs(text: str):
    """Split a line of Markdown into [(text, style), ...] runs."""
    text = re.sub(r'\$([^$]+)\$', r'\1', text)          # $x^2$ -> x^2
    runs = []
    for part in re.split(r'(`[^`]+`|\*\*[^*]+\*\*)', text):
        if not part:
            continue
        if part.startswith('`'):
            runs.append((part[1:-1], 'mono'))
        elif part.startswith('**'):
            runs.append((part[2:-2], 'bold'))
        else:
            runs.append((part, 'regular'))
    return runs


def _markdown_blocks(md: str):
    """Split question Markdown into [('para'|'bullets'|'code', content), ...].
    A code fence always stands on its own, with or without blank lines."""
    md = (md or '').replace('\r\n', '\n').strip()
    code_blocks = []

    def stash(m):
        code_blocks.append(m.group(2).rstrip('\n'))
        return f'\n\n@@CODEBLOCK{len(code_blocks) - 1}@@\n\n'

    text = re.sub(r'```([a-zA-Z0-9]*)\n([\s\S]*?)```', stash, md)
    blocks = []
    for block in re.split(r'\n\s*\n', text):
        trimmed = block.strip()
        if not trimmed:
            continue
        m = re.fullmatch(r'@@CODEBLOCK(\d+)@@', trimmed)
        lines = trimmed.split('\n')
        if m:
            blocks.append(('code', code_blocks[int(m.group(1))]))
        elif re.match(r'^\s*-\s+', lines[0]):
            # Group lines into bullet items: a line starting with "- " begins
            # a new item; any other line (e.g. an indented wrapped
            # continuation of the previous item's text) is appended to the
            # current item instead of being mistaken for a non-list paragraph.
            items = []
            for line in lines:
                bm = re.match(r'^\s*-\s+(.*)', line)
                if bm:
                    items.append(bm.group(1))
                elif items:
                    items[-1] += ' ' + line.strip()
                else:
                    items.append(line.strip())
            blocks.append(('bullets', items))
        else:
            blocks.append(('para', trimmed.replace('\n', ' ')))
    return blocks


class _PdfWriter:
    """Lays out text top-to-bottom on pages, then writes the PDF file."""

    def __init__(self, title: str):
        self.title = title
        self.pages = []           # list of lists of PDF drawing commands
        self.y = 0

    def new_page(self):
        self.pages.append([])
        self.y = PAGE_H - MARGIN

    def ensure_space(self, height: float):
        if self.y - height < MARGIN:
            self.new_page()

    def text(self, x: float, y: float, text: str, style: str, size: float, gray: float = 0):
        name, _ = _FONTS[style]
        self.pages[-1].append(
            f'{gray} g BT /{name} {size} Tf {x:.2f} {y:.2f} Td {_pdf_string(text)} Tj ET'
        )

    def rect(self, x, y, w, h, fill_gray, stroke_gray):
        self.pages[-1].append(
            f'{fill_gray} g {stroke_gray} G 0.75 w {x:.2f} {y:.2f} {w:.2f} {h:.2f} re B'
        )

    def line(self, x1, y1, x2, y2, width=1):
        self.pages[-1].append(f'0 G {width} w {x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S')

    # --- higher-level pieces ---

    def heading(self, text: str, size: float, note: str = '', rule: bool = False):
        self.ensure_space(size + 30)
        self.y -= size
        self.text(MARGIN, self.y, text, 'bold', size)
        if note:
            x = MARGIN + _text_width(text + ' ', 'bold', size)
            self.text(x, self.y, note, 'regular', size * 0.7, gray=0.4)
        self.y -= 6
        if rule:
            self.line(MARGIN, self.y, PAGE_W - MARGIN, self.y, 1.5)
        self.y -= 12

    def paragraph(self, md_text: str, indent: float = 0, bullet: bool = False):
        # break the runs into words, keeping each word's style
        words = []
        for run_text, style in _inline_runs(md_text):
            for w in re.findall(r'\S+|\s+', run_text):
                words.append((w, style))
        width = TEXT_W - indent
        lines, current, current_w = [], [], 0
        for w, style in words:
            if w.isspace():
                if current:
                    current.append((' ', style))
                    current_w += _text_width(' ', style, BODY_SIZE)
                continue
            w_width = _text_width(w, style, BODY_SIZE)
            if current and current_w + w_width > width:
                while current and current[-1][0] == ' ':
                    current.pop()
                lines.append(current)
                current, current_w = [], 0
            current.append((w, style))
            current_w += w_width
        if current:
            lines.append(current)

        for i, line in enumerate(lines):
            self.ensure_space(BODY_LEADING)
            self.y -= BODY_LEADING
            if bullet and i == 0:
                self.text(MARGIN + indent - 12, self.y + 3, '\u2022', 'regular', BODY_SIZE)
            x = MARGIN + indent
            for w, style in line:
                size = BODY_SIZE if style != 'mono' else BODY_SIZE - 0.5
                self.text(x, self.y + 3, w, style, size)
                x += _text_width(w, style, size)
        self.y -= 8

    def code(self, code_text: str):
        # wrap long lines at the box width (monospace, so just count characters)
        max_chars = int((TEXT_W - 2 * CODE_PAD) / (0.6 * CODE_SIZE))
        lines = []
        for line in code_text.expandtabs(4).split('\n'):
            line = line.rstrip()
            while len(line) > max_chars:
                lines.append(line[:max_chars])
                line = '    ' + line[max_chars:]
            lines.append(line)

        # draw the box a page at a time, so a long block can continue onto
        # the next page (but never start a box with fewer than 3 lines left)
        self.ensure_space(min(len(lines), 3) * CODE_LEADING + 2 * CODE_PAD)
        while lines:
            fit = int((self.y - MARGIN - 2 * CODE_PAD) // CODE_LEADING)
            chunk, lines = lines[:fit], lines[fit:]
            box_h = len(chunk) * CODE_LEADING + 2 * CODE_PAD
            self.rect(MARGIN, self.y - box_h, TEXT_W, box_h, 0.955, 0.8)
            text_y = self.y - CODE_PAD
            for line in chunk:
                text_y -= CODE_LEADING
                if line:
                    self.text(MARGIN + CODE_PAD, text_y + 3, line, 'mono', CODE_SIZE)
            self.y -= box_h + 12
            if lines:
                self.new_page()

    def markdown(self, md: str):
        for kind, content in _markdown_blocks(md):
            if kind == 'code':
                self.code(content)
            elif kind == 'bullets':
                for item in content:
                    self.paragraph(item, indent=18, bullet=True)
            else:
                self.paragraph(content)

    def save(self, path: Path):
        # page numbers at the bottom of every page
        total = len(self.pages)
        for i, commands in enumerate(self.pages, start=1):
            label = f'{self.title} - page {i} of {total}'
            x = (PAGE_W - _text_width(label, 'regular', 8)) / 2
            commands.append(
                f'0.5 g BT /F1 8 Tf {x:.2f} {MARGIN / 2:.2f} Td {_pdf_string(label)} Tj ET'
            )

        # PDF objects: 1 catalog, 2 page list, 3-5 fonts, 6 info, then a
        # (page, contents) pair for each page
        objects = {}
        page_ids = []
        next_id = 7
        for commands in self.pages:
            page_id, content_id = next_id, next_id + 1
            next_id += 2
            page_ids.append(page_id)
            stream = zlib.compress('\n'.join(commands).encode('latin-1'))
            objects[content_id] = (
                f'<< /Length {len(stream)} /Filter /FlateDecode >>\nstream\n'.encode('latin-1')
                + stream + b'\nendstream'
            )
            objects[page_id] = (
                f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PAGE_W} {PAGE_H}] '
                f'/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >> >> '
                f'/Contents {content_id} 0 R >>'
            ).encode('latin-1')
        objects[1] = b'<< /Type /Catalog /Pages 2 0 R >>'
        kids = ' '.join(f'{p} 0 R' for p in page_ids)
        objects[2] = f'<< /Type /Pages /Kids [{kids}] /Count {len(page_ids)} >>'.encode('latin-1')
        for obj_id, style in zip((3, 4, 5), ('regular', 'bold', 'mono')):
            objects[obj_id] = (
                f'<< /Type /Font /Subtype /Type1 /BaseFont /{_FONTS[style][1]} '
                f'/Encoding /WinAnsiEncoding >>'
            ).encode('latin-1')
        objects[6] = f'<< /Title {_pdf_string(self.title)} >>'.encode('latin-1')

        out = bytearray(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n')
        offsets = {}
        for obj_id in sorted(objects):
            offsets[obj_id] = len(out)
            out += f'{obj_id} 0 obj\n'.encode('latin-1') + objects[obj_id] + b'\nendobj\n'
        xref_at = len(out)
        count = max(objects) + 1
        out += f'xref\n0 {count}\n0000000000 65535 f \n'.encode('latin-1')
        for obj_id in range(1, count):
            out += f'{offsets[obj_id]:010d} 00000 n \n'.encode('latin-1')
        out += (f'trailer\n<< /Size {count} /Root 1 0 R /Info 6 0 R >>\n'
                f'startxref\n{xref_at}\n%%EOF\n').encode('latin-1')
        path.write_bytes(bytes(out))


def write_all_questions_pdf(parsed, pdf_path: Path, title: str, include_solutions: bool):
    """Write one PDF with every question (and, if include_solutions is True,
    its sample solution), each question starting on a new page."""
    pdf = _PdfWriter(title)
    for i, (number, sol_path, _header, question_md, solution_code) in enumerate(parsed):
        pdf.new_page()
        if i == 0:
            pdf.heading(title, 20)
            pdf.y -= 6
        # questions-only PDF names the qN.py stub file students work in
        file_name = sol_path.name if include_solutions else f'q{number}.py'
        pdf.heading(f'Question {number}', 15, note=f'({file_name})', rule=True)
        pdf.markdown(question_md)
        if include_solutions:
            pdf.y -= 4
            pdf.heading('Sample Solution', 12)
            pdf.code(solution_code)
    pdf.save(pdf_path)
    return pdf_path


def slugify(text: str) -> str:
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', text.strip().lower()).strip('-')
    return slug or 'presentation'


# ---------------------------------------------------------------------------
# HTML template for the presentation page
# ---------------------------------------------------------------------------
# The generated page is this template with __TITLE__, __DONE_KEY__, and the
# <!-- QUESTION_BLOCKS --> marker filled in. Edit it here to change the
# page's look or behaviour.

TEMPLATE_HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<style>
  :root {
    --bg: #f4f5f7;
    --panel: #ffffff;
    --text: #1a1a1a;
    --accent: #2563eb;
    --accent-dark: #1d4ed8;
    --done: #16a34a;
    --border: #d8dce3;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }
  header {
    padding: 20px 30px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
    border-bottom: 1px solid var(--border);
    background: var(--panel);
  }
  header h1 {
    font-size: 1.4rem;
    margin: 0;
  }
  .question-nav {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }
  .q-btn {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 10px 18px;
    font-size: 1.1rem;
    border-radius: 8px;
    border: 2px solid var(--border);
    background: var(--panel);
    cursor: pointer;
    transition: all 0.15s ease;
  }
  .q-btn:hover { border-color: var(--accent); }
  .q-btn.active { border-color: var(--accent); background: #eaf1ff; }
  .q-btn.done { border-color: var(--done); }
  .q-btn .check {
    width: 22px;
    height: 22px;
    border-radius: 50%;
    border: 2px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.9rem;
    color: transparent;
    flex-shrink: 0;
  }
  .q-btn.done .check {
    background: var(--done);
    border-color: var(--done);
    color: white;
  }
  main {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    padding: 40px 30px 60px;
  }
  .stage {
    max-width: 1000px;
    width: 100%;
  }
  .placeholder {
    text-align: center;
    font-size: 1.6rem;
    color: #888;
    margin-top: 80px;
  }
  .question-block {
    font-size: 2.1rem;
    font-weight: 700;
    line-height: 1.5;
    text-align: left;
  }
  .question-block p { margin: 0 0 0.7em; }
  .question-block ul { margin: 0.5em 0 0.9em 1.4em; }
  .question-block li { margin-bottom: 0.3em; }
  .question-block pre {
    background: #1e1e2e;
    color: #f5f5f5;
    padding: 18px 22px;
    border-radius: 10px;
    overflow-x: auto;
    font-size: 1.2rem;
    font-weight: 400;
  }
  .question-block code {
    background: #e8eaf0;
    padding: 2px 8px;
    border-radius: 5px;
    font-size: 0.85em;
    font-weight: 400;
  }
  .question-block pre code { background: none; padding: 0; }
  .controls {
    display: flex;
    gap: 14px;
    margin: 30px 0;
    flex-wrap: wrap;
  }
  button.action {
    font-size: 1.15rem;
    padding: 14px 26px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    font-weight: 600;
  }
  .btn-answer {
    background: var(--accent);
    color: white;
  }
  .btn-answer:hover { background: var(--accent-dark); }
  .btn-answer.showing { background: #4b5563; }
  .btn-done {
    background: var(--panel);
    border: 2px solid var(--done);
    color: var(--done);
  }
  .btn-done.active {
    background: var(--done);
    color: white;
  }
  .answer-panel {
    display: none;
    margin-top: 10px;
    padding: 26px 30px;
    background: #fffbe6;
    border: 2px solid #f2d675;
    border-radius: 12px;
    font-size: 1.5rem;
    line-height: 1.5;
  }
  .answer-panel.visible { display: block; }
  .answer-panel h2 {
    margin-top: 0;
    font-size: 1.1rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #92700f;
  }
  .answer-panel pre {
    background: #1e1e2e;
    color: #f5f5f5;
    padding: 16px 20px;
    border-radius: 10px;
    overflow-x: auto;
    font-size: 1.15rem;
  }
  .answer-panel code {
    background: #eee0b0;
    padding: 2px 8px;
    border-radius: 5px;
  }
  .answer-panel pre code { background: none; padding: 0; }
  .no-answer {
    font-style: italic;
    color: #888;
  }
  .file-tag {
    font-size: 0.85rem;
    color: #999;
    margin-top: -18px;
    margin-bottom: 20px;
  }
  sup, sub { font-size: 0.7em; }
</style>
</head>
<body>
<header>
  <h1>__TITLE__</h1>
  <div class="question-nav" id="questionNav"></div>
</header>
<main>
  <div class="stage" id="stage">
    <div class="placeholder">Select a question above to display it.</div>
  </div>
</main>

<!--
  ============================================================================
  QUESTION DATA -- GENERATED, DO NOT EDIT BY HAND
  ============================================================================
  This file was generated by generate_presentation.py from the qN.md files
  in this folder (q1.md, q2.md, q3.md, ...). Each question's markdown is
  embedded below in a <script type="text/plain"> block, which the browser
  never runs or displays -- it's just a plain-text container.

  To change a question: edit its qN.md file, then re-run
      python3 generate_presentation.py
  to regenerate this HTML file.

  To add a question: add a new qN.md file (q5.md, q6.md, ...) with a
  "## Question" section and an optional "## Sample Solution" section,
  then re-run the script.

  To remove a question: delete its qN.md file and re-run the script.

  Do not use the literal text "</script>" inside a question's markdown --
  that's the only thing that would break it.
  ============================================================================
-->

<!-- QUESTION_BLOCKS -->

<script>
function splitSections(text) {
  text = (text || '').replace(/\r\n/g, '\n');
  const qMatch = text.match(/##\s*Question\s*\n([\s\S]*?)(?=\n##\s*Sample Solution|$)/);
  const sMatch = text.match(/##\s*Sample Solution\s*\n([\s\S]*)/);
  const question = qMatch ? qMatch[1].trim() : text.trim();
  const solution = sMatch ? sMatch[1].trim() : '';
  return { question: question, solution: solution };
}

function loadQuestionsFromPage() {
  const blocks = document.querySelectorAll('script.qfile');
  const loaded = [];
  blocks.forEach(function(block) {
    const sections = splitSections(block.textContent);
    loaded.push({
      id: block.dataset.id,
      file: block.dataset.file,
      label: block.dataset.label,
      question: sections.question,
      solution: sections.solution
    });
  });
  return loaded;
}

const QUESTIONS = loadQuestionsFromPage();

const DONE_KEY = '__DONE_KEY__';
function loadDone() {
  try {
    return new Set(JSON.parse(localStorage.getItem(DONE_KEY) || '[]'));
  } catch (e) {
    return new Set();
  }
}
function saveDone(set) {
  try {
    localStorage.setItem(DONE_KEY, JSON.stringify(Array.from(set)));
  } catch (e) {}
}
let doneSet = loadDone();
let currentId = null;
let answerShown = false;

function escapeHtml(str) {
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function renderInlineMarkup(text) {
  text = text.replace(/\$([^$]+)\$/g, function(_, inner) {
    let out = inner;
    out = out.replace(/\^\{([^}]+)\}/g, '<sup>$1</sup>');
    out = out.replace(/\^([A-Za-z0-9])/g, '<sup>$1</sup>');
    out = out.replace(/_\{([^}]+)\}/g, '<sub>$1</sub>');
    out = out.replace(/_([A-Za-z0-9])/g, '<sub>$1</sub>');
    return out;
  });
  text = text.replace(/`([^`]+)`/g, '<code>$1</code>');
  text = text.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  return text;
}

function renderMarkdownLite(md) {
  md = (md || '').replace(/\r\n/g, '\n').trim();
  if (!md) return '';
  const fenceRegex = /```([a-zA-Z0-9]*)\n([\s\S]*?)```/g;
  const codeBlocks = [];
  const placeholderText = md.replace(fenceRegex, function(_, lang, code) {
    const idx = codeBlocks.length;
    codeBlocks.push(escapeHtml(code.replace(/\n$/, '')));
    // blank lines around the placeholder so a code block always stands on
    // its own, even if the question has no blank line before or after it
    return '\n\n@@CODEBLOCK' + idx + '@@\n\n';
  });
  const blocks = placeholderText.split(/\n\s*\n/);
  let html = '';
  for (const block of blocks) {
    const trimmed = block.trim();
    if (!trimmed) continue;
    const codeMatch = trimmed.match(/^@@CODEBLOCK(\d+)@@$/);
    if (codeMatch) {
      html += '<pre><code>' + codeBlocks[parseInt(codeMatch[1], 10)] + '</code></pre>';
      continue;
    }
    const lines = trimmed.split('\n');
    if (/^\s*-\s+/.test(lines[0])) {
      // Group lines into bullet items: a line starting with "- " begins a
      // new item; any other line (e.g. an indented wrapped continuation of
      // the previous item's text) is appended to the current item instead
      // of being mistaken for a non-list paragraph.
      const items = [];
      lines.forEach(function(l) {
        const m = l.match(/^\s*-\s+(.*)/);
        if (m) {
          items.push(m[1]);
        } else if (items.length) {
          items[items.length - 1] += ' ' + l.trim();
        } else {
          items.push(l.trim());
        }
      });
      html += '<ul>' + items.map(function(item) {
        return '<li>' + renderInlineMarkup(escapeHtml(item)) + '</li>';
      }).join('') + '</ul>';
    } else {
      const joined = trimmed.replace(/\n/g, ' ');
      html += '<p>' + renderInlineMarkup(escapeHtml(joined)) + '</p>';
    }
  }
  return html;
}

function buildNav() {
  const nav = document.getElementById('questionNav');
  nav.innerHTML = '';
  QUESTIONS.forEach(function(q) {
    const btn = document.createElement('button');
    btn.className = 'q-btn' + (doneSet.has(q.id) ? ' done' : '') + (q.id === currentId ? ' active' : '');
    btn.type = 'button';
    const check = document.createElement('span');
    check.className = 'check';
    check.textContent = '✓';
    check.title = 'Toggle done';
    check.addEventListener('click', function(e) {
      e.stopPropagation();
      toggleDone(q.id);
    });
    const label = document.createElement('span');
    label.textContent = q.label;
    btn.appendChild(check);
    btn.appendChild(label);
    btn.addEventListener('click', function() {
      showQuestion(q.id);
    });
    nav.appendChild(btn);
  });
}

function toggleDone(id) {
  if (doneSet.has(id)) {
    doneSet.delete(id);
  } else {
    doneSet.add(id);
  }
  saveDone(doneSet);
  buildNav();
  if (id === currentId) renderStage();
}

function showQuestion(id) {
  currentId = id;
  answerShown = false;
  buildNav();
  renderStage();
}

function renderStage() {
  const stage = document.getElementById('stage');
  const q = QUESTIONS.find(function(x) { return x.id === currentId; });
  if (!q) {
    stage.innerHTML = '<div class="placeholder">Select a question above to display it.</div>';
    return;
  }
  const isDone = doneSet.has(q.id);
  const hasSolution = q.solution && q.solution.trim().length > 0;
  let html = '';
  html += '<div class="file-tag">' + q.file + '</div>';
  html += '<div class="question-block">' + renderMarkdownLite(q.question) + '</div>';
  html += '<div class="controls">';
  html += '<button type="button" class="action btn-answer' + (answerShown ? ' showing' : '') + '" id="answerToggle">' + (answerShown ? 'Hide Answer' : 'Show Answer') + '</button>';
  html += '<button type="button" class="action btn-done' + (isDone ? ' active' : '') + '" id="doneToggle">' + (isDone ? '✓ Marked Done' : 'Mark as Done') + '</button>';
  html += '</div>';
  html += '<div class="answer-panel' + (answerShown ? ' visible' : '') + '" id="answerPanel">';
  html += '<h2>Sample Solution</h2>';
  html += hasSolution ? renderMarkdownLite(q.solution) : '<p class="no-answer">No sample solution provided for this question.</p>';
  html += '</div>';
  stage.innerHTML = html;

  document.getElementById('answerToggle').addEventListener('click', function() {
    answerShown = !answerShown;
    renderStage();
  });
  document.getElementById('doneToggle').addEventListener('click', function() {
    toggleDone(q.id);
  });
}

if (QUESTIONS.length === 0) {
  document.getElementById('stage').innerHTML = '<div class="placeholder">No question blocks found in this page.</div>';
} else {
  buildNav();
  renderStage();
}
</script>
</body>
</html>
'''


def main():
    script_dir = Path(__file__).resolve().parent

    parser = argparse.ArgumentParser(
        description='Make an HTML practice-question presentation (plus student\n'
                    'files, a README, and PDFs) from q1_sol.py, q2_sol.py, ... files.',
        epilog=HELP_TEXT,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        '-d', '--dir', default=str(script_dir),
        help='Folder containing q1_sol.py, q2_sol.py, ... (default: folder this script lives in)',
    )
    parser.add_argument(
        '-o', '--output', default='presentation.html',
        help='Output HTML filename, written into --dir unless given as an absolute '
             'path (default: presentation.html)',
    )
    parser.add_argument(
        '-t', '--title', default='Practice Questions',
        help='Page title / header text (default: "Practice Questions")',
    )
    args = parser.parse_args()

    directory = Path(args.dir).resolve()

    if not directory.is_dir():
        sys.exit(f"Error: {directory} is not a folder.")

    question_files = find_question_files(directory)
    if not question_files:
        print(f"Error: no question files (q1_sol.py, q2_sol.py, ...) were found in:\n"
              f"    {directory}\n", file=sys.stderr)
        parser.print_help(sys.stderr)
        sys.exit(1)

    template = TEMPLATE_HTML

    parsed = []
    for number, sol_path in question_files:
        header_source, question_md, solution_code = parse_solution_file(sol_path)
        parsed.append((number, sol_path, header_source, question_md, solution_code))

    blocks_html = '\n\n'.join(
        build_qfile_block(number, sol_path, question_md, solution_code)
        for number, sol_path, _header_source, question_md, solution_code in parsed
    )

    output_arg = Path(args.output)
    output_path = output_arg if output_arg.is_absolute() else directory / output_arg
    done_key = 'presentationAI_done_' + slugify(output_path.stem)

    page = template.replace(MARKER, blocks_html)
    page = page.replace('__TITLE__', html.escape(args.title))
    page = page.replace('__DONE_KEY__', done_key)

    output_path.write_text(page, encoding='utf-8')

    stub_paths = write_stub_files(parsed, directory)
    questions_pdf = write_all_questions_pdf(
        parsed,
        output_path.with_name(f'{directory.name}_questions.pdf'),
        f"{directory.name} Practice Questions",
        include_solutions=False,
    )
    solutions_pdf = write_all_questions_pdf(
        parsed,
        output_path.with_name(f'{directory.name}_questions_and_solutions.pdf'),
        f"{directory.name} Practice Questions and Solutions",
        include_solutions=True,
    )
    readme_path = write_readme(parsed, directory, questions_pdf, solutions_pdf)

    names = ', '.join(p.name for _, p in question_files)
    print(f"Wrote {output_path} from {len(question_files)} question file(s): {names}")
    print(f"Wrote {len(stub_paths)} stub file(s): " + ', '.join(p.name for p in stub_paths))
    print(f"Wrote {questions_pdf}")
    print(f"Wrote {solutions_pdf}")
    print(f"Wrote {readme_path}")


if __name__ == '__main__':
    main()
