# q2_sol.py

"""
A warehouse labels its boxes with product codes like "BX-4471". Sometimes the
scanner misreads one character, and staff need to correct it. Write a function
called fix_code(code, position, correct_char) that returns (not prints!) the
corrected code. 

Assume that code is always a string of at least 7 characters, that position is a
valid index, and correct_char is a single character.

For example:

- fix_code("BX-4A71", 4, "9") returns "BX-4971"
- fix_code("TH-8328", 3, "7") returns "TH-7328"
- fix_code("XX-1111", 0, "R") returns "RX-1111"

Use the following code to test your fix_code function.

```
if fix_code('BX-4A71', 4, '9') == 'BX-4971':
    print("Test 1 passed")
else:
    print("Test 1 FAILED!!!")

if fix_code('TH-8328', 3, '7') == 'TH-7328':
    print("Test 2 passed")
else:
    print("Test 2 FAILED!!!")

if fix_code('XX-1111', 0, 'R') == 'RX-1111':
    print("Test 3 passed")
else:
    print("Test 3 FAILED!!!")
```
"""

def fix_code(code, position, correct_char):
    return code[:position] + correct_char + code[position+1:]

if fix_code('BX-4A71', 4, '9') == 'BX-4971':
    print("Test 1 passed")
else:
    print("Test 1 FAILED!!!")

if fix_code('TH-8328', 3, '7') == 'TH-7328':
    print("Test 2 passed")
else:
    print("Test 2 FAILED!!!")

if fix_code('XX-1111', 0, 'R') == 'RX-1111':
    print("Test 3 passed")
else:
    print("Test 3 FAILED!!!")
