# q2_sol.py

"""
Write a program that reads in the lengths of the two legs of a right triangle (a
and b in the diagram)and then computes the length of the hypotenuse using the
fact that c^2 = a^2 + b^2.

```
      /|
  c  / |  a
    /  |
   /___|
     b
```

Here's a sample run:

```
What is a? 3.5
What ib b? 6

The hypotenuse c is 6.946221994724902
```
"""

import math

a = float(input('What is a? '))
b = float(input('What is b? '))
c = math.sqrt(a**2 + b**2)
print('The hypotenuse c is', c)
