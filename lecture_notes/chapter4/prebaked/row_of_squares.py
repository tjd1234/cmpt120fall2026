# row_of_squares.py

import turtle

def square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)

def row_of_squares(num_squares, length):
    for i in range(num_squares):
        square(length)
        turtle.forward(length)

turtle.Screen().setup(startx=900, starty=0)
turtle.teleport(-200, 0)
row_of_squares(10, 50)

turtle.done()
