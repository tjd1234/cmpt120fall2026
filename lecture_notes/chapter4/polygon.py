# polygon.py

import turtle

# doc-string
def polygon(num_sides, length):
    """Draws a regular polygon with the given number of sides and side length.
    
    num_sides: integer number of sides
    length: length of the sides
    """
    angle = 360 / num_sides
    for i in range(num_sides):
        turtle.forward(length)
        turtle.right(angle)

# put the turtle window in a more convenient location
turtle.Screen().setup(startx=900, starty=0)

polygon(3, 100)
polygon(4, 100)
polygon(5, 100)
polygon(6, 100)
polygon(7, 100)

# turtle.done()
