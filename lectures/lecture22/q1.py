# q1.py

"""
SFU term codes are 4-digit numbers, where each number has a specific meaning.
For example, the term code 1267 means Fall 2026 because:

- the first digit is a 1 (for this century)
- the next two digits are 26, the last two digits of the year 2026
- the last digit is a 7, which is the semester code for Fall

Using your semesters dictionary, write code that takes a semester name and a
year and prints the term code. It should read in the semester name, the year,
and then print the term code. You do *not* need to repeatedly ask the user, i.e.
it can stop after the printing the term code.

3 Sample Runs

```
Enter semester: Fall
Enter year: 2026
Fall 2026 term code: 1267

Enter semester: Spring
Enter year: 2027
Spring 2027 term code: 1271

Enter semester: Summer
Enter year: 2026
Summer 2026 term code: 1264
```

Use this dictionary in your program:

```
codes = {'spring': 1, 'summer': 4, 'fall': 7}
```
"""
