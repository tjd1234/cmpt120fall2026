# spiral1.py

import turtle

turtle.setup(startx=10, starty=10)
turtle.speed(0)

#
# TODO: Re-write this loop using a for-loop.
#
# for distance in range(1, 200, 2):
#     turtle.forward(distance)
#     turtle.left(100)

distance = 1
while distance < 400:
    turtle.forward(distance)
    turtle.left(91)
    distance += 2

turtle.done()
