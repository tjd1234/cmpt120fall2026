# q2_sol.py

"""
SFU gives semesters a code number as follows:

```
Semester   Code
---------------
 Spring      1
 Summer      4
 Fall        7
```

Write a program that stores the semesters and their codes in a dictionary. The
semesters are the keys, and the codes are the values. 

Then write a program that repeatedly asks the user to enter a semester, and,
using the dictionary, prints the corresponding code. It should stop when they
press the <return> key. If the user enters an unknown semester, then print a
helpful error message.

Important: the *case* of the semester name does not matter. So, for example,
"spring", "Spring", and "SPRING" should all be treated the same. The output 
the semester name is always capitalized, e.g. "Summer", "Spring, "Fall".

Sample Run

```
Enter semester: Spring
Spring code: 1

Enter semester: SUMMER
Summer code: 4

Enter semester: Winter
Unknown semester

Enter semester: <return>
All done!
```

"""
codes = {'spring': 1, 'summer': 4, 'fall': 7}

while True:
    semester = input('Enter semester: ')
    semester = semester.strip().lower()
    if semester == '':
        break
    elif semester in codes:
        code = codes[semester]
        print(f'{semester.capitalize()} code: {code}')
    else:
        print('Unknown semester')
    print()

print('All done!')
