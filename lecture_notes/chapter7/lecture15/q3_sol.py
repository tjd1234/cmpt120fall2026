# q3_sol.py

"""
# q4_sol.py

During wildfire season, air quality is reported using the Air Quality Health
Index (AQHI). Here's a simplified version of the advice for strenuous outdoor
activity:

```
| AQHI      | At-risk people   | Everyone else    |
|-----------|------------------|------------------|
| below 1   | Invalid          | Invalid          |
| 1 to 3    | Low: normal      | Low: normal      |
| 4 to 6    | Moderate: reduce | Moderate: normal |
| 7 to 10   | High: avoid      | High: reduce     |
| above 10  | Very high: avoid | Very high: avoid |
```
Write a program that asks for the AQHI reading (as an int) and whether the user
is at risk (y or n), and then prints the advice from the table.

(At-risk people include people with heart or lung problems, the elderly, and 
children.)

Sample Run 1

```
AQHI? 5
At risk (y/n)? n
Moderate: normal
```

Sample Run 2

```
AQHI? 8
At risk (y/n)? y
High: avoid
```

"""

aqhi = int(input('AQHI? '))
at_risk = input('At risk (y/n)? ')

if aqhi < 1:
    print('Invalid')
elif aqhi <= 3:
    print('Low: normal')
elif aqhi <= 6 and at_risk == 'y':
    print('Moderate: reduce')
elif aqhi <= 6:
    print('Moderate: normal')
elif aqhi <= 10 and at_risk == 'y':
    print('High: avoid')
elif aqhi <= 10:
    print('High: reduce')
else:
    print('Very high: avoid')
