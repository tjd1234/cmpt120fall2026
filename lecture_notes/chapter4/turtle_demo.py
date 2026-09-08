# demo.py

import turtle

def snowflake(length):
    for i in range(8):
        turtle.left(45)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)

def square(length):
    for i in range(4):
        turtle.forward(i * length)
        turtle.right(90)
        turtle.pensize(5 * (i + 1))

turtle.color('blue')
for i in range(10):
    square(25)
    turtle.right(36)


turtle.done()
