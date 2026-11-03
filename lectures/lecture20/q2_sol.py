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

Test your program by calling fix_code with the given examples and printing the
results as shown.

Sample Run

```
BX-4A71 -> BX-4971
TH-8328 -> TH-7328
XX-1111 -> RX-1111
```
"""

def fix_code(code, position, correct_char):
    return code[:position] + correct_char + code[position+1:]

print(f"BX-4A71 -> {fix_code('BX-4A71', 4, '9')}")
print(f"TH-8328 -> {fix_code('TH-8328', 3, '7')}")
print(f"XX-1111 -> {fix_code('XX-1111', 0, 'R')}")
