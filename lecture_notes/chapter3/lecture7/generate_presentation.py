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
README.md in the same folder with a table of contents linking to each
qN.py stub and, in brackets, its qN_sol.py solution file.

To make a new presentation:
    1. Write q1_sol.py, q2_sol.py, q3_sol.py, ... in a folder, each with a
       docstring (the question, in Markdown) followed by the solution code.
    2. Run this script (optionally with -o to name the output file).
    3. Open the generated HTML file in a browser.

To update a presentation after changing a question or its solution, just
edit its qN_sol.py file and re-run this script -- it overwrites the output
file, the qN.py stub files, and README.md.

Note: qN.py and README.md are generated files, derived from qN_sol.py --
re-running this script overwrites them, so don't hand-edit them.
"""
import argparse
import ast
import html
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


def write_readme(parsed, directory: Path):
    """Write README.md with a table of contents linking each qN.py to its qN_sol.py."""
    lines = ["# Table of Contents", ""]
    for number, sol_path, _header_source, _question_md, _solution_code in parsed:
        stub_name = f"q{number}.py"
        sol_name = sol_path.name
        lines.append(f"- [{stub_name}]({stub_name}) ([{sol_name}]({sol_name}))")
    lines.append("")
    readme_path = directory / "README.md"
    readme_path.write_text('\n'.join(lines), encoding='utf-8')
    return readme_path


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
    readme_path = write_readme(parsed, directory)

    names = ', '.join(p.name for _, p in question_files)
    print(f"Wrote {output_path} from {len(question_files)} question file(s): {names}")
    print(f"Wrote {len(stub_paths)} stub file(s): " + ', '.join(p.name for p in stub_paths))
    print(f"Wrote {readme_path}")


if __name__ == '__main__':
    main()
