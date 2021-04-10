"""
You are given the following information, but you may prefer to do some research
for yourself.
- 1 Jan 1900 was a Monday.
- Thirty days has September, April, June and November. All the rest have
thirty-one, Saving February alone, Which has twenty-eight, rain or shine. And
on leap years, twenty-nine.
- A leap year occurs on any year evenly divisble by 4, but not on a centuary
unless it is divisble by 400.
"""

import datetime

start_date = datetime.date(1901, 1, 1)
end_date = datetime.date(2000, 12, 31)
delta = datetime.timedelta(days=1)
num = 0

while start_date <= end_date:
    if start_date.day == 1 and start_date.weekday() == 6:
        num += 1
    start_date += delta

print(num)
