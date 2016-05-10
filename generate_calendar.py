# TODO
# gui input
# parse inputs
# include adjacent days outside the given month
# handle edge case formatting errors
# remove dependence on Sultanik's style

import calendar

import subprocess
import os
import tempfile
import shutil


def generate_latex(month, year, firstweekday):
    """Return a string of latex code that would compile into a pdf calendar"""
    latex_code = ""
    latex_code += "\n\\documentclass[landscape,a4paper]{article}\n\\usepackage{calendar}" \
                  "\n\\usepackage[landscape,margin=0.6in]{geometry}\n\\begin{document}\n\\pagestyle{empty}\n\\noindent"
    # calendar.sty is one-based with 1 is Sunday while Lib/calendar.py is zero-based with 0 is Monday, 6 is Sunday
    # we will use the convention from Lib/calendar.py for input and convert this to work with calendar.sty
    latex_firstweekday = (firstweekday + 2) % 7
    if latex_firstweekday == 0:
        latex_firstweekday = 7
    latex_code += "\n\\StartingDayNumber=" + str(latex_firstweekday)
    latex_code += "\n\\begin{center}\n\\textsc{\LARGE " + calendar.month_name[month] + " }% month" \
                  "\n\\textsc{\LARGE " + str(year) + "} % year\n\\end{center}"
    latex_code += "\n\\begin{calendar}{\hsize}"
    c = calendar.Calendar()
    c.setfirstweekday(firstweekday)
    for day in c.itermonthdays(year, month):
        if day == 0:
            latex_code += "\n\\setcounter{calendardate}{0}\n\\BlankDay"
        else:
            latex_code += "\n\\day{}{\\vspace{2.5cm}}"
    latex_code += "\n\\finishCalendar\n\\end{calendar}\n\\end{document}"
    return latex_code


def build_pdf(file_name, latex_code):
    """Build a pdf from a string of latex code"""

    cwd = os.getcwd()
    temp = tempfile.mkdtemp()
    shutil.copy("calendar.sty", temp)
    os.chdir(temp)

    f = open("temp.tex", "w")
    f.write(latex_code)
    f.close()

    proc = subprocess.Popen(["pdflatex", "temp.tex"])
    subprocess.Popen(["pdflatex", latex_code])
    proc.communicate()

    os.rename("temp.pdf", file_name + ".pdf")
    shutil.copy(file_name + ".pdf", cwd)
    shutil.rmtree(temp)


def build_calendar(month, year, firstweekday):
    """Build a pdf calendar"""
    latex_code = generate_latex(month, year, firstweekday)
    build_pdf("calendar_" + calendar.month_name[month] + "_" + str(year), latex_code)
