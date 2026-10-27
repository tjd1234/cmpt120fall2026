# q1_sol.py

"""
Write a program that reads a string the user and then prints the letter and
index value in the style shown.

```
Enter a string: hello

s = 'hello'
s[0] is 'h'
s[1] is 'e'
s[2] is 'l'
s[3] is 'l'
s[4] is 'o'
```
"""

s = input('Enter a string: ')
print()
print(f"s = '{s}'")
for i in range(len(s)):
    letter = s[i]
    print(f"s[{i}] is '{letter}'")
