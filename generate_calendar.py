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

import calendar


# c = calendar.TextCalendar()
# c.setfirstweekday(5)
# c.prmonth(2016, 5)
#
# c = calendar.Calendar()
# c.setfirstweekday(5)
# for day in c.itermonthdates(2016, 5):
#     print day,
# print "\n"
# for day in c.itermonthdays2(2016, 5):
#     print day,
# print "\n"
# for day in c.itermonthdays(2016, 5):
#     print day,
# print "\n"


def generate_calendar(month, year, firstweekday):
    """
    given a month and year, creates a string of latex code that will compile into a pdf calendar for that month
    """
    latex_file = ""
    latex_file += "\n\\documentclass[landscape,a4paper]{article}\n\\usepackage{calendar}" \
                  "\n\\usepackage[landscape,margin=0.6in]{geometry}\n\\begin{document}\n\\pagestyle{empty}\n\\noindent"
    # calendar.sty is one-based with 1 is Sunday while Lib/calendar.py is zero-based with 0 is Monday, 6 is Sunday
    # we will use the convention from Lib/calendar.py for input and convert this to work with calendar.sty
    firstweekday = (firstweekday + 2) % 7
    if firstweekday == 0:
        firstweekday = 7
    latex_file += "\n\\StartingDayNumber=" + str(firstweekday)
    latex_file += "\n\\begin{center}\n\\textsc{\LARGE " + str(month) + " }% month" \
                  "\n%\\textsc{\LARGE " + str(year) + "} % year\n\\end{center}"
    latex_file += "\n\\begin{calendar}{\hsize}"
    c = calendar.Calendar()
    c.setfirstweekday(firstweekday)
    for day in c.itermonthdays(year, month):
        if day == 0:
            latex_file += "\n\\setcounter{calendardate}{0}\n\\BlankDay"
        else:
            latex_file += "\n\\day{}{\\vspace{2.5cm}}"
    latex_file += "\n\\finishCalendar\n\\end{calendar}\n\\end{document}"
    return latex_file
