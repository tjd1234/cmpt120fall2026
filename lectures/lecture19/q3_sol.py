# q3_sol.py

"""
Weekly Step Tracker

Your fitness tracker shows how many steps you took each day, and you want a
quick summary of your week.

Write a program that asks the user for their step count on each of 7 days. Use
input() and append each number to a list called steps. Then it prints:

- the total number of steps for the week
- the fewest steps taken on any one day and the most steps taken on any one day
- the average steps per day, rounded to 1 digit after the decimal point
- all 7 step counts from smallest to largest, one per line

Sample Run

```
Steps on day 1: 6421
Steps on day 2: 10250
Steps on day 3: 3890
Steps on day 4: 8125
Steps on day 5: 12034
Steps on day 6: 7560
Steps on day 7: 5013

 Total steps: 53293
Fewest steps: 3890
  Most steps: 12034
     Average: 7613.3

Smallest to largest:
3890
5013
6421
7560
8125
10250
12034
```
"""

#
# read in the step counts from the user
#
steps = []
for i in range(7):
    n = int(input(f'Steps on day {i + 1}: '))
    steps.append(n)

#
# calculate and print the stats
#
total = sum(steps)
least = min(steps)
most = max(steps)
average = total / len(steps)
print()
print(f' Total steps: {total}')
print(f'Fewest steps: {least}')
print(f'  Most steps: {most}')
print(f'     Average: {average:.1f}')

#
# print the step counts from smallest to largest
#
steps.sort()
print()
print('Smallest to largest:')
for n in steps:
    print(n)
