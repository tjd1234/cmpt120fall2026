# q2_sol.py

"""
SFU term codes are 4-digit numbers, where each number has a specific meaning.
For example, the term code 1267 means Fall 2026 because:

- the first digit is a 1 (for this century)
- the next two digits are 26, the last two digits of the year 2026
- the last digit is a 7, which is the semester code for Fall

The semester codes are:

```
Semester   Code
---------------
 Spring      1
 Summer      4
 Fall        7
```

Write a program that reads in a term code and prints the year and term as shown.

Sample Runs

```
Term code: 1267
Fall 2026

Term code: 1161
Spring 2016

Term code: 1274
Summer 2027

Term code: <enter>
done!
```
"""
codes = {1: 'Spring', 4: 'Summer', 7: 'Fall'}

while True:
    # get the term code from the user
    term_code = input("Enter term code: ")
    term_code = term_code.strip()

    if term_code == '':
        break

    # get the year from the term code
    year = "20" + term_code[1] + term_code[2]

    # get the term from the term code
    term_num = int(term_code[3])
    term = codes[term_num]

    # print the year and term
    print(f"{term} {year}")
    print()

print("done!")
