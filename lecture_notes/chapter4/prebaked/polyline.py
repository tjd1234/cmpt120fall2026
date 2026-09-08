# polyline.py

import turtle

def polyline(n, length, angle):
    """Draws line segments with the given length and angle between them.
    
    n: integer number of line segments
    length: length of the line segments
    angle: angle between segments (in degrees)
    """    
    for i in range(n):
        turtle.forward(length)
        turtle.left(angle)

polyline(5, 100, 144)    # 5-pointed star
polyline(5, 100, 45)     # 5 sides of an octagon
polyline(5, 100, 70)     # an unfinished pentagon
polyline(25, 100, 100)   # a nice pattern

#
# polygon can be implemented using polyline
#
# def polygon(num_sides, length):
#     angle = 360.0 / num_sides
#     polyline(num_sides, length, angle)

turtle.done()
