#!/usr/bin/python3

# TODO include adjacent days outside the given month
# TODO handle edge case formatting errors
# TODO remove dependence on Sultanik's style

import argparse
import calendar
import subprocess
from pathlib import Path


def generate_latex(month: int, year: int, firstweekday: int) -> str:
    """Return a string of latex code that would compile into a pdf calendar"""

    latex_code = ""
    latex_code += (
        "\n\\documentclass[landscape,a4paper]{article}\n\\usepackage{calendar}"
        "\n\\usepackage[landscape,margin=0.6in]{geometry}\n\\begin{document}\n\\pagestyle{empty}\n\\noindent"
    )
    # calendar.sty is one-based where 1 is Sunday
    # while Lib/calendar.py is zero-based where 0 is Monday and 6 is Sunday
    # use the convention from Lib/calendar.py for input and convert this to work with calendar.sty
    latex_firstweekday = (firstweekday + 2) % 7
    if latex_firstweekday == 0:
        latex_firstweekday = 7
    latex_code += "\n\\StartingDayNumber=" + str(latex_firstweekday)
    latex_code += (
        "\n\\begin{center}\n\\textsc{\\LARGE " + calendar.month_name[month] + " } % month"
        "\n\\textsc{\\LARGE " + str(year) + "} % year\n\\end{center}"
    )
    latex_code += "\n\\begin{calendar}{\\hsize}"

    cal = calendar.Calendar()
    cal.setfirstweekday(firstweekday)
    for day in cal.itermonthdays(year, month):
        if day == 0:
            latex_code += "\n\\setcounter{calendardate}{0}\n\\BlankDay"
        else:
            latex_code += "\n\\day{}{\\vspace{2.5cm}}"

    latex_code += "\n\\finishCalendar\n\\end{calendar}\n\\end{document}"
    return latex_code


def build_pdf(file_name: str, latex_code: str) -> None:
    """Build a pdf from a string of latex code"""

    Path("temp.tex").write_text(latex_code)

    subprocess.call(
        ["pdflatex", "temp.tex"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

    Path("temp.pdf").rename(file_name + ".pdf")
    Path("temp.aux").unlink()
    Path("temp.log").unlink()
    Path("temp.tex").unlink()


def build_calendar(year: int, month: int, firstweekday: int, tex: bool = False) -> None:
    """Build a pdf calendar"""

    latex_code = generate_latex(month, year, firstweekday)
    file_name = f"calendar_{year}-{month:02}"
    if tex:
        Path(f"{file_name}.tex").write_text(latex_code)
    else:
        build_pdf(file_name, latex_code)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build a monthly calendar")
    parser.add_argument("year", type=int, help="The year")
    parser.add_argument(
        "month", type=int, help="The month as an integer [1-12]"
    )
    parser.add_argument(
        "firstweekday", type=int, help="The first weekday [0 = Monday]"
    )
    parser.add_argument("--tex", action="store_true", help="Whether to generate a tex file instead of a pdf")
    args = parser.parse_args()
    build_calendar(args.year, args.month, args.firstweekday, args.tex)

