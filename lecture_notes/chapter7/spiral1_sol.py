# spiral1_sol.py

import turtle

turtle.setup(startx=10, starty=10)
turtle.speed(0)

distance = 1
while distance < 200:
    turtle.forward(distance)
    turtle.left(91)
    distance += 2

turtle.done()
