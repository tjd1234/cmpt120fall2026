# q1_sol.py

"""
Write a program that reads a phrase from the user prints sandwiched between two
lines of dash characters as shown in the sample run:

```
Enter a phrase: Hello, world!

-------------
Hello, world!
-------------
```
"""

phrase = input('Enter a phrase: ')
line = '-' * len(phrase)
print(line)
print(phrase)
print(line)
