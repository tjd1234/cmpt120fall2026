# dist.py

#
# This function prints the distance between two points (using the Pythagorean theorem).
#

import math

def print_dist(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    result = math.sqrt(dx * dx + dy * dy)
    print(f'The distance between ({x1}, {y1}) and ({x2}, {y2}) is {result}')

print_dist(-3.1, 2, 4, 6)