import calendar
import datetime
import time

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2021,2,3,2))

print(calendar.monthcalendar(2021,2))
print(calendar.calendar(2021))

day_of_the_week = calendar.weekday(2021,2,10)
print(day_of_the_week)

is_leap = calendar.isleap(2021)
print(is_leap)

how_many_leap_days = calendar.leapdays(1998,2021)
print(how_many_leap_days)