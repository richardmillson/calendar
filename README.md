calendar
============
[![Build Status](https://travis-ci.org/richardmillson/calendar.svg)](https://travis-ci.org/richardmillson/calendar)

Build a pdf calendar of your month.

Requires pdflatex, which you can get by downloading texlive https://www.tug.org/texlive/ or most other tex installations.

Uses the latex 'calendar' package by Evan Sultanik, included here as calendar.sty.

## Usage

To generate just the pdf file for the calendar, run
```shell
uv run python generate_calendar.py 2026 5 0
```
[An example pdf output](examples/calendar_2026-05.pdf)
This requires having pdflatex installed.

To generate just a tex file for the calendar, run
```shell
uv run python generate_calendar.py 2026 5 0 --tex
```
[An example tex output](examples/calendar_2026-05.tex)
