# q2.py

"""
Write a program that repeatedly asks the user for a date in the format
YYYY-MM-DD and prints the same date in the format DD/MM/YYYY. The program should
end with the user pressing <enter> with no date entered.

You can assume the user always types the date in the correct format.

```
Enter a date (YYYY-MM-DD): 2026-10-25
25/10/2026
Enter a date (YYYY-MM-DD): 1992-08-14
14/08/1992
Enter a date (YYYY-MM-DD): <enter>
Done!
```
"""

while True:
    date = input('Enter a date (YYYY-MM-DD): ')
    date = date.strip()
    if date == '':
        break
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]

    # DD/MM/YYYY
    print(f'{day}/{month}/{year}')

print('Done!')
