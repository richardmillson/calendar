import calendar

# c = calendar.TextCalendar()
# c.setfirstweekday(5)
# c.prmonth(2016, 5)

c = calendar.Calendar()
c.setfirstweekday(5)
for day in c.itermonthdates(2016, 5):
    print day
for day in c.itermonthdays2(2016, 5):
    print day
for day in c.itermonthdays(2016, 5):
    print day

# def generate_calendar(month, year):
# 	""" given a month and year, will create a pdf calendar for that month """
