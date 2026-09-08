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

def square(length):
    rectangle(length, length)

# put the turtle window in a more convenient location
turtle.Screen().setup(startx=900, starty=0)

square(10)
square(50)
square(100)

turtle.done()
