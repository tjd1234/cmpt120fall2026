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
solution file, plus a link to the printable version described below.

Finally, it writes a printable version, <output>_printable.html (e.g.
presentation_printable.html): one static page with every question and its
sample solution, one after the other, titled "<folder name> Practice
Questions", each under a clear "Question N" heading and starting on a new
page when printed.

To make a new presentation:
    1. Write q1_sol.py, q2_sol.py, q3_sol.py, ... in a folder, each with a
       docstring (the question, in Markdown) followed by the solution code.
    2. Run this script (optionally with -o to name the output file).
    3. Open the generated HTML file in a browser.

To update a presentation after changing a question or its solution, just
edit its qN_sol.py file and re-run this script -- it overwrites the output
file, the qN.py stub files, README.md, and the printable HTML file.

Note: qN.py, README.md, and the printable HTML file are generated files, derived from qN_sol.py --
re-running this script overwrites them, so don't hand-edit them.
"""
import argparse
import ast
import html
import os
import re
import sys
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


def write_readme(parsed, directory: Path, printable_path: Path):
    """Write README.md with a list linking each qN.py to its qN_sol.py,
    followed by a link to the printable page of all questions."""
    lines = [f"# {directory.name} Questions and Answers", ""]
    for number, sol_path, _header_source, _question_md, _solution_code in parsed:
        stub_name = f"q{number}.py"
        sol_name = sol_path.name
        lines.append(f"- [{stub_name}]({stub_name}) ([{sol_name}]({sol_name}))")
    # link relative to the README (as_posix() keeps forward slashes for Markdown)
    printable_link = Path(os.path.relpath(printable_path, directory)).as_posix()
    lines.append("")
    lines.append(f"All questions and solutions on one page: [{printable_link}]({printable_link})")
    lines.append("")
    readme_path = directory / "README.md"
    readme_path.write_text('\n'.join(lines), encoding='utf-8')
    return readme_path


# ---------------------------------------------------------------------------
# Printable version: every question and its solution in one static HTML page
# ---------------------------------------------------------------------------
# These functions are a Python port of renderMarkdownLite() in template.html,
# so the printable page renders the question Markdown the same way the
# presentation does -- but ahead of time, with no JavaScript needed to print.

def _render_inline_markup(text: str) -> str:
    def math(m):
        out = m.group(1)
        out = re.sub(r'\^\{([^}]+)\}', r'<sup>\1</sup>', out)
        out = re.sub(r'\^([A-Za-z0-9])', r'<sup>\1</sup>', out)
        out = re.sub(r'_\{([^}]+)\}', r'<sub>\1</sub>', out)
        out = re.sub(r'_([A-Za-z0-9])', r'<sub>\1</sub>', out)
        return out
    text = re.sub(r'\$([^$]+)\$', math, text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    return text


def _escape(text: str) -> str:
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def render_markdown_lite(md: str) -> str:
    """Convert the small Markdown subset used in questions (paragraphs,
    "- " bullet lists, ``` code fences, `code`, **bold**, $x^2$) to HTML."""
    md = (md or '').replace('\r\n', '\n').strip()
    if not md:
        return ''
    code_blocks = []

    def stash(m):
        code_blocks.append(_escape(re.sub(r'\n$', '', m.group(2))))
        # blank lines around the placeholder so a code block always stands
        # on its own, even if the question has no blank line before it
        return f'\n\n@@CODEBLOCK{len(code_blocks) - 1}@@\n\n'

    text = re.sub(r'```([a-zA-Z0-9]*)\n([\s\S]*?)```', stash, md)
    parts = []
    for block in re.split(r'\n\s*\n', text):
        trimmed = block.strip()
        if not trimmed:
            continue
        m = re.fullmatch(r'@@CODEBLOCK(\d+)@@', trimmed)
        if m:
            parts.append(f'<pre><code>{code_blocks[int(m.group(1))]}</code></pre>')
            continue
        lines = trimmed.split('\n')
        if all(re.match(r'^\s*-\s+', line) for line in lines):
            items = ''.join(
                '<li>' + _render_inline_markup(_escape(re.sub(r'^\s*-\s+', '', line))) + '</li>'
                for line in lines
            )
            parts.append(f'<ul>{items}</ul>')
        else:
            parts.append('<p>' + _render_inline_markup(_escape(trimmed.replace('\n', ' '))) + '</p>')
    return '\n'.join(parts)


PRINTABLE_CSS = """
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    color: #1a1a1a;
    max-width: 800px;
    margin: 30px auto;
    padding: 0 20px;
    line-height: 1.5;
  }
  h1 { font-size: 1.6rem; margin-bottom: 30px; }
  .question { margin-bottom: 40px; }
  .question h2 {
    font-size: 1.35rem;
    border-bottom: 2px solid #1a1a1a;
    padding-bottom: 4px;
  }
  .question h3 { font-size: 1.1rem; margin-top: 24px; }
  .file-name { font-weight: normal; color: #666; font-size: 1rem; }
  pre {
    background: #f4f5f7;
    border: 1px solid #d8dce3;
    border-radius: 5px;
    padding: 10px 14px;
    white-space: pre-wrap;
    font-size: 0.9rem;
  }
  code {
    font-family: Menlo, Consolas, "Courier New", monospace;
    background: #f0f0f0;
    padding: 1px 4px;
    border-radius: 3px;
  }
  pre code { background: none; padding: 0; }
  sup, sub { font-size: 0.7em; }
  @media print {
    body { margin: 0; max-width: none; }
    /* start each question on a new page */
    .question + .question { break-before: page; }
    pre { break-inside: avoid; }
    h2, h3 { break-after: avoid; }
  }
"""


def write_printable(parsed, output_path: Path, title: str):
    """Write one static HTML page with every question and its sample
    solution, one after the other -- meant for printing."""
    sections = []
    for number, sol_path, _header_source, question_md, solution_code in parsed:
        sections.append(
            '<section class="question">\n'
            f'<h2>Question {number} <span class="file-name">({html.escape(sol_path.name)})</span></h2>\n'
            f'{render_markdown_lite(question_md)}\n'
            '<h3>Sample Solution</h3>\n'
            f'<pre><code>{_escape(solution_code)}</code></pre>\n'
            '</section>'
        )
    page = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
        f'<title>{html.escape(title)}</title>\n'
        f'<style>{PRINTABLE_CSS}</style>\n</head>\n<body>\n'
        f'<h1>{html.escape(title)}</h1>\n\n'
        + '\n\n'.join(sections)
        + '\n</body>\n</html>\n'
    )
    output_path.write_text(page, encoding='utf-8')
    return output_path


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
    printable_path = write_printable(
        parsed,
        output_path.with_name(output_path.stem + '_printable.html'),
        f"{directory.name} Practice Questions",
    )
    readme_path = write_readme(parsed, directory, printable_path)

    names = ', '.join(p.name for _, p in question_files)
    print(f"Wrote {output_path} from {len(question_files)} question file(s): {names}")
    print(f"Wrote {len(stub_paths)} stub file(s): " + ', '.join(p.name for p in stub_paths))
    print(f"Wrote {printable_path}")
    print(f"Wrote {readme_path}")


if __name__ == '__main__':
    main()
