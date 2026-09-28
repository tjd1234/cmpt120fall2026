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
lives in, and writes presentation.html into that same folder, using
template.html (kept alongside this script) for the page's styling and
behaviour.

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
        elif all(re.match(r'^\s*-\s+', line) for line in lines):
            blocks.append(('bullets', [re.sub(r'^\s*-\s+', '', line) for line in lines]))
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


def main():
    script_dir = Path(__file__).resolve().parent

    parser = argparse.ArgumentParser(
        description=__doc__,
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
    parser.add_argument(
        '--template', default=None,
        help='Template HTML file to use (default: template.html next to this script)',
    )
    args = parser.parse_args()

    directory = Path(args.dir).resolve()
    template_path = Path(args.template).resolve() if args.template else script_dir / 'template.html'

    if not directory.is_dir():
        sys.exit(f"Error: {directory} is not a folder.")
    if not template_path.is_file():
        sys.exit(f"Error: template file not found at {template_path}")

    question_files = find_question_files(directory)
    if not question_files:
        sys.exit(f"Error: no q1_sol.py, q2_sol.py, ... files found in {directory}")

    template = template_path.read_text(encoding='utf-8')
    if MARKER not in template:
        sys.exit(f"Error: template {template_path} is missing the {MARKER} marker.")

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
