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

def grid(num_cols, length):
    start_x, start_y = turtle.position()
    for row in range(num_cols):
        row_of_squares(num_cols, length)
        turtle.teleport(start_x, start_y + (row + 1)*length)

turtle.Screen().setup(startx=900, starty=0)
turtle.teleport(-200, 0)
grid(3, 50)

turtle.done()
