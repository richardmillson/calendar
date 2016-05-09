# TODO
# generate latex code to work within Sultanik's template
# compile latex code inside python
# parse inputs
# gui input
# accept firstweekday as input
# clean up temporary files
# remove dependence on Sultanik's template
# recover day number from datetime object to include adjacent days outside the given month
#


def generate_latex(month, year, firstweekday):
    """
    given a month and year, creates a string of latex code that will compile into a pdf calendar for that month
    """
    import calendar

    latex_code = ""
    latex_code += "\n\\documentclass[landscape,a4paper]{article}\n\\usepackage{calendar}" \
                  "\n\\usepackage[landscape,margin=0.6in]{geometry}\n\\begin{document}\n\\pagestyle{empty}\n\\noindent"
    # calendar.sty is one-based with 1 is Sunday while Lib/calendar.py is zero-based with 0 is Monday, 6 is Sunday
    # we will use the convention from Lib/calendar.py for input and convert this to work with calendar.sty
    print firstweekday
    firstweekday = (firstweekday + 2) % 7
    if firstweekday == 0:
        firstweekday = 7
    print firstweekday
    latex_code += "\n\\StartingDayNumber=" + str(firstweekday)
    latex_code += "\n\\begin{center}\n\\textsc{\LARGE " + str(month) + " }% month" \
                  "\n%\\textsc{\LARGE " + str(year) + "} % year\n\\end{center}"
    latex_code += "\n\\begin{calendar}{\hsize}"
    c = calendar.Calendar()
    c.setfirstweekday(firstweekday)
    for day in c.itermonthdays(year, month):
        print day,
        if day == 0:
            latex_code += "\n\\setcounter{calendardate}{0}\n\\BlankDay"
        else:
            latex_code += "\n\\day{}{\\vspace{2.5cm}}"
    latex_code += "\n\\finishCalendar\n\\end{calendar}\n\\end{document}"
    return latex_code


def build_pdf(pdfname, tex):
    """
    build a pdf from a string
    """
    import subprocess
    import os
    import tempfile
    import shutil

    current = os.getcwd()
    temp = tempfile.mkdtemp()
    shutil.copy("calendar.sty", temp)
    os.chdir(temp)

    f = open("temp.tex", "w")
    f.write(tex)
    f.close()

    proc = subprocess.Popen(["pdflatex", "temp.tex"])
    subprocess.Popen(["pdflatex", tex])
    proc.communicate()

    os.rename("temp.pdf", pdfname + ".pdf")
    shutil.copy(pdfname + ".pdf", current)
    shutil.rmtree(temp)

    # f = open("temp.tex", "w")
    # f.write(tex)
    # f.close()
    #
    # proc = subprocess.Popen(["pdflatex", "temp.tex"])
    # subprocess.Popen(["pdflatex", tex])
    # proc.communicate()
    #
    # os.rename("temp.pdf", pdfname + ".pdf")


def build_calendar(month, year, firstweekday):
    latex_code = generate_latex(month, year, firstweekday)
    build_pdf(str(month), latex_code)
