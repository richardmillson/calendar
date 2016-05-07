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
    latex_file = "\n\\documentclass[landscape,a4paper]{article}\n\\usepackage{calendar}\n\\usepackage[landscape,margin=0.6in]{geometry}\n\\begin{document}\n\\pagestyle{empty}\n\\noindent\n\\begin{calendar}{\hsize}"
    c = calendar.Calendar()
    c.setfirstweekday(firstweekday)
    for day in c.itermonthdays(year, month):
        # latex_file += str(day)
        pass
    latex_file += "\n\\finishCalendar\n\\end{calendar}\n\\end{document}"
    return latex_file
