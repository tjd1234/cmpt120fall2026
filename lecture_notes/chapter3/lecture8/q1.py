# q1.py

"""
Make a Python version of the math function f(x) = 2x + 1. Use it print the
values f(2), f(5), and f(1000). Then ask the user to enter a number and print
the value of f(x) as shown.

```
5
11
2001
Enter a number: 2.6
f(2.6) = 6.2
```
"""

def f(x):
    return 2 * x + 1

print(f(2))
print(f(5))

result = f(1000)
print(result)

x = float(input('Enter a number: '))

# f(2.6) = 6.2
print('f(' + str(x) + ') = ' + str(f(x)))
print(f'f({x}) = {f(x)}')














