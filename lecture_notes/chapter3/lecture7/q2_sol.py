# q2_sol.py

"""
Write a program that reads 3 ints from the user, and then prints then in order
from smallest to biggest:

```
1st int: 5
2nd int: 0
3rd int: 2

In order: 0, 2, 5
```

Your program should work for any three integers, and it should only use
features covered so far in the course, like basic arithmetic, printing, etc.
Hint: Research Python's min and max functions.
"""

a = int(input('1st int: '))
b = int(input('2nd int: '))
c = int(input('3rd int: '))

first = min(a, b, c)
third = max(a, b, c)

# there are other ways to calculate second, but they are tricky
second = a + b + c - first - third

print(f'In order: {first}, {second}, {third}')



