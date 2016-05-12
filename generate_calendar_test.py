
from generate_calendar import *

firstweekday = 5
year = 2016
month = 5


def test_generate_latex():
    latex_code = generate_latex(month, year, firstweekday)


def test_build_pdf():
    pass


def test_build_calendar():
    build_calendar(month, year, firstweekday)
    file_name = "calendar_" + calendar.month_name[month] + "_" + str(year) + ".pdf"
    # print os.getcwd()
    # print file_name
    assert(os.path.isfile(file_name))


test_generate_latex()
test_build_pdf()
test_build_calendar()
