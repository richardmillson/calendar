
from generate_calendar import *

firstweekday = 5
year = 2020
month = 2


def test_generate_latex():
    latex_code = generate_latex(year=year, month=month, firstweekday=firstweekday)


def test_build_pdf():
    pass


def test_build_calendar():
    build_calendar(year=year, month=month, firstweekday=firstweekday)
    file_name = "calendar_" + calendar.month_name[month] + "_" + str(year) + ".pdf"
    assert(Path(file_name).exists())


test_generate_latex()
test_build_pdf()
test_build_calendar()

