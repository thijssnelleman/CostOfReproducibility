"""Code for generating LateX output for a paper."""
from pathlib import Path
from collections.abc import Iterable

def latex_table(columns: list[str], rows: list[list[str]], values: list,
                column_char = "c", column_sep = "", header_sep = r"\hline",
                centering = True,
                label="", caption="") -> str:
    """Create a LateX table."""
    row_title_factor = 1 if isinstance(rows[0], str) or not isinstance(rows[0], Iterable) else len(rows[0])
    open_cmd = "\\begin{table}\n"
    if centering:
        open_cmd += "\\centering\n"
    open_cmd += "\\begin{tabular}" + "{" + "l" * row_title_factor + "|" + (column_char + column_sep) * len(columns) + "}\n"
    header = " & " * row_title_factor + " & ".join(columns) + "\\\\\n"
    if header_sep:
        header = header + header_sep + "\n"

    lines = []
    for row_title, row_value in zip(rows, values):
        if isinstance(row_title, list):
            row_title = " & ".join([str(item) for item in row_title])
        line = f"\t{row_title} & " + " & ".join([str(v) for v in row_value]) + r"\\"
        lines.append(line)
    ender = []
    if caption:
        ender.append("\\caption{" + caption + "}")
    if label:
        ender.append("\\label{" + label + "}")
    return open_cmd + header + "\n".join(lines) + "\n\\end{tabular}\n" + "\n".join(ender) + "\n\\end{table}\n"

def compile_latex(text: str, output: Path) -> None:
    """Compile LateX .tex file."""
    if not isinstance(output, Path):
        output = Path(output)
    if output.root != "latex":
        output = Path("latex") / output
    if not output.parent.exists():
        output.parent.mkdir(parents=True)
    tex_output = output.with_suffix(".tex")
    with tex_output.open("w") as f:
        f.write(text)
    return
