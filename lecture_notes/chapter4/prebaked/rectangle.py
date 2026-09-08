# rectangle.py

import turtle

def rectangle(width, height):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)

rectangle(10, 5)
rectangle(50, 20)
rectangle(100, 175)

turtle.done()