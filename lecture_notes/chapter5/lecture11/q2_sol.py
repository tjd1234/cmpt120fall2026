# q2_sol.py

"""
Write a program that asks the user to enter the side-length of a perfectly
square field, and then prints the area and the perimeter of the field.

However, you must do it by creating and using two functions: one that calculates
the area of the square (given the side length), and one that calculates the
perimeter of the square (given the side length). Each of these functions should
return (not print!) their result.

Use these functions in a sensible way in your program.

``` 
How long is the field? 6 

The area is 36. 
The perimeter is 24.
```

"""

def square_area(size):
    return size * size

def square_perimeter(size):
    return 4 * size

size = float(input("How long is the field? "))
area = square_area(size)
perimeter = square_perimeter(size)
print(f"The area is {area}.")
print(f"The perimeter is {perimeter}.")
