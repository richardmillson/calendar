
from generate_calendar import *

# from Tkinter import Tk
#
#
# def copy(s, root):
#     root.clipboard_clear()
#     root.clipboard_append(s)


firstweekday = 6
year = 2016
month = 5


def test_generate_calendar():
    latex_code = generate_calendar(month, year, firstweekday)
    print latex_code
    # root = Tk()
    # copy(latex_code, root)
    # root.destroy()


def test_build_pdf():
    pass

test_generate_calendar()
test_build_pdf()

