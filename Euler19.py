# Program to count the number of Sundays from 1 Jan 1901 to Dec 2000

import datetime

total = 0
start = time.time()
day = 1

for year in range(1901, 2001):
    for month in range(1, 13):
        if datetime.date(year, month, day).strftime("%A") == 'Sunday':
            total += 1



print(total)

# answer: 171
