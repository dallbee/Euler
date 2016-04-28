"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
fdays = [1]
sunday = 7

for y in range(1901, 2000):
    mdays[1] = 29 if y % 4 == 0 else 28
    for d in mdays:
        fdays.append(fdays[-1] + d)


sundays = filter(lambda x: x % 7 == 0, fdays)
print(len(list(sundays)))