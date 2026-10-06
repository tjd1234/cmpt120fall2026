# q2_sol.py

"""
Write a program that asks the user to enter the side-length of a perfectly
square field, and then prints the area and the perimeter of the field.

However, you must do it by creating and using two functions: one that calculates
are (given the side length), and one that calculates the perimeter (given the
side length). Each of these functions should return (not print!) their result.

Use these functions in a sensible way in your program.

```
How long is the field? 6
The area is 36. 
The perimeter is 24.
```

"""

def area(size):
    return size * size

def perimeter(size):
    return 4 * size

size = int(input("How long is the field? "))
area = area(size)
perimeter = perimeter(size)
print(f"The area is {area}.")
print(f"The perimeter is {perimeter}.")
