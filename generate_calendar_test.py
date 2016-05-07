from generate_calendar import *


def test_generate_calendar():
    firstweekday = 5
    year = 2016
    month = 5
    print generate_calendar(month, year, firstweekday)


test_generate_calendar()