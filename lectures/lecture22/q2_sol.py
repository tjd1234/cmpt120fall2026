# q2_sol.py

"""
Write a program that repeatedly asks the user to enter a term *code number* and
the prints the corresponding semester name. It should stop when the user types
<return>, and print a helpful message if an invalid code is typed. Use a
dictionary to efficiently store the semester codes.

Here are the semester codes:

```
Semester   Code
---------------
 Spring      1
 Summer      4
 Fall        7
```

Sample Run

```
Enter semester code: 4
4 is Summer

Enter semester code: 8
8 is invalid

Enter semester code: 1
1 is Spring

Enter semester code: <return>
All done!
```
"""

codes = {1: 'Spring', 4: 'Summer', 7: 'Fall'}

while True:
    code = input('Enter semester code: ')
    if code == '':
      break
    code = int(code.strip())
    if code in codes:
        semester = codes[code]
        print(f'{code} is {semester}')
    else:
        print(f'{code} is invalid')
    print()

print('All done!')
