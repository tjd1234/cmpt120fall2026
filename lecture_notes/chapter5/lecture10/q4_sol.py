# q4_sol.py

"""
During the summer, a neighborhood has these rules for lawn watering:

- houses with even street numbers may water their lawn only on even-numbered
  days
  
- houses with odd street numbers may water their lawn only on odd-numbered days

Write a program that asks the user to enter a street number (like 503 or
1944) and a day number (Monday is 1, Tuesday is 2, ..., Sunday is 7), and then
prints whether or not that house may water their lawn that day.

As an extra challenge, write and use a function called `can_water(street_number,
day)` that returns `True` if the house may water their lawn that day, and `False`
otherwise.

Sample run 1
```
Enter a street number: 503
Enter a day number: 1
You can water your lawn today.
```

Sample run 2
```
Enter a street number: 1944
Enter a day number: 2
You can water your lawn today.
```

Sample run 3
```
Enter a street number: 1944
Enter a day number: 3
You cannot water your lawn today.
```
"""

def can_water(street_number, day):
    if street_number % 2 == 0:
        return day % 2 == 0
    else:
        return day % 2 != 0

street_number = int(input("Enter a street number: "))
day = int(input("Enter a day number: "))
if can_water(street_number, day):
    print("You can water your lawn today.")
else:
    print("You cannot water your lawn today.")
