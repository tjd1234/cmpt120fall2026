# circle.py

import turtle

def polygon(num_sides, length):
    """Draws a regular polygon with the given number of sides and side length.
    
    num_sides: integer number of sides
    length: length of the sides
    """
    angle = 360 / num_sides
    for i in range(num_sides):
        turtle.forward(length)
        turtle.right(angle)

import math  # for math.pi

def circle(radius):
    """Draws a circle with the given radius.
    
    radius: radius of the circle
    """
    circumference = 2 * math.pi * radius
    num_sides = 30
    length = circumference / num_sides
    polygon(num_sides, length)

circle(25)
circle(50)
circle(100)
circle(500)  # edges are visible

turtle.done()
