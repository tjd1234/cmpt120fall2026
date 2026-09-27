# q6_sol.py

"""
Write a program that asks the user to enter an int (called n)that is 0 or
greater. Then, starting at 1, print the ints from 1 to n on the screen in a box
as shown. Use the print_in_box(word) function from the previous question.

```
Enter an int: 3

+-+
|1|
+-+

+-+
|2|
+-+

+-+
|3|
+-+
```
"""

def print_in_bars(word):    
    print(f'|{word}|')

def print_in_box(word):
    bar = '+' + '-' * len(word) + '+'
    print(bar)
    print_in_bars(word)
    print(bar)

n = int(input("Enter an int: "))
print()
for i in range(1, n+1):
    print_in_box(str(i))
    print()
