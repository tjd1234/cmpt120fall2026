# trig_helper.py

"""
Write a program that reads in a floating pointer number, and then prints:

- the sine and cosine (from the math module)
- the tangent of the number using the formula sin(x) / cos(x)
- the tangent using tan(x) (from the math module)

Why do you think the two tangent values are sometimes a little bit different? Is
this a problem? Why or why not?

Sample run:

    Enter a number: 10
    sin(10.0):
    -0.5440211108893698

    cos(10.0):
    -0.8390715290764524

    sin(10.0) / cos(10.0):
    0.6483608274590866

    tan(10.0):
    0.6483608274590867

"""

import math

x = float(input('Enter a number: '))
sin = math.sin(x)
cos = math.cos(x)
tan1 = sin / cos
tan2 = math.tan(x)
print(f'\nsin({x}):\n{sin}')
print(f'\ncos({x}):\n{cos}')
print(f'\nsin({x}) / cos({x}):\n{tan1}')
print(f'\ntan({x}):\n{tan2}')
