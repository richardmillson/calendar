
from generate_calendar import *

import calendar

firstweekday = 6
year = 2016
month = 5


# c = calendar.TextCalendar()
# c.setfirstweekday(firstweekday)
# c.prmonth(year, month)
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


def test_generate_latex():
    latex_code = generate_latex(month, year, firstweekday)
    print latex_code


def test_build_pdf():
    pass


def test_build_calendar():
    build_calendar(month, year, firstweekday)


# test_generate_latex()
# test_build_pdf()
test_build_calendar()
