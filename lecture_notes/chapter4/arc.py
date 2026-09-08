# arc.py

import turtle
import math


def polyline(n, length, angle):
    """Draws line segments with the given length and angle between them.

    n: integer number of line segments
    length: length of the line segments
    angle: angle between segments (in degrees)
    """
    for i in range(n):
        turtle.forward(length)
        turtle.left(angle)


def arc(radius, angle):
    """Draws a circular arc with the given radius and angle.

    radius: radius of the arc
    angle: angle of the arc (in degrees)
    """
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(n, length, step_angle)

# put the turtle window in a more convenient location
turtle.Screen().setup(startx=900, starty=0)

turtle.color("red")
arc(100, 180)  # half circle

turtle.teleport(0, 0)
turtle.color("blue")
arc(200, 90)  # quarter circle

turtle.teleport(0, 0)
turtle.color("green")
arc(50, 360)  # full circle

#
# circle can be implemented using arc
#
# def circle(radius):
#     arc(radius, 360)

turtle.done()
