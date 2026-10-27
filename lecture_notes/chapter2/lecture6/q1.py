# q1.py

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

# get input
phrase = input('Enter a phrase: ')

# process it
line = '-' * len(phrase)

# output
print(line)
print(phrase)
print(line)
