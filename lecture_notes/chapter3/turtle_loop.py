# turtle_loop.py

#
# Draws a pattern using a for-loop and turtle graphics.
# 

import turtle

def triangle():
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)

for i in range(10):
    triangle()

turtle.done()