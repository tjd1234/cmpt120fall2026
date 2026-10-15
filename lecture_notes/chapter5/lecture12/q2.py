# q2.py

"""
Python has a built-in function called `abs(x)` that returns the absolute value
of `x`. For example:

- `abs(5)` returns 5
- `abs(-5)` returns 5
- `abs(0)` returns 0

Write a function called `my_abs(x)` that returns the absolute value of `x`
without using the built-in `abs` function. Build your function from basic Python
features.

In addition, write some testing code that asks the user to enter a number and
verifies that `my_abs(x)` always returns the same value as `abs(x)`.

Sample Run 1

```
Enter a number: 5.2

my_abs(5.2) returns 5.2
   abs(5.2) returns 5.2
Good: they're the same!
```

Sample Run 2

```
Enter a number: -5.2

my_abs(-5.2) returns 5.2
   abs(-5.2) returns 5.2
Good: they're the same!
```

If you've implemented `my_abs(x)` correctly, then the last line should always be
"Good: they're the same!". But if there is a bug in your `my_abs(x)` function,
it should print "Bad: they're different!":

Sample Run 3

```
Enter a number: -1

my_abs(-1) returns -1
    abs(1) returns 1
Bad: they're different!
```

"""

def my_abs(x):
    if x < 0:
        return -x
    else: # x >= 0
        return x


x = float(input('Enter a float: '))

result_my_abs = my_abs(x)
result_abs = abs(x)
print(f'my_abs({x}) returns {result_my_abs}')
print(f'   abs({x}) returns {result_abs}')

if result_my_abs == result_abs:
    print("Good: they're the same!")
else:
    print("Bad: they're different!")



