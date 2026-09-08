# triangle2.py

#
# This program calculates the hypotenuse of a right triangle
# given the lengths of the two sides:
#
#      |\
#      | \
#      |  \          Pythagorean theorem:
#    a |   \  hypotenuse = sqrt(a ** 2 + b ** 2)
#      |    \
#      |     \
#      +------+
#         b
#

import math

a = 3
b = 4

hypotenuse = math.sqrt(a ** 2 + b ** 2)

print(hypotenuse)
