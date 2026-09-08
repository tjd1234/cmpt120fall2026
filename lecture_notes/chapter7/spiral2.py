# spiral2_sol.py

import turtle

turtle.setup(startx=10, starty=10)
turtle.speed(0)

#
# TODO: Modify this so that the loop ends when the turtle is off the screen.
# turtle.position() returns the current (x, y) position of the turtle, and
# turtle.window_width() and turtle.window_height() give the dimensions of the
# screen.
#
# Hint: Write a function called off_screen that returns True if the turtle is
# off the screen, and False otherwise.
#
distance = 1
while distance < 200:
    turtle.forward(distance)
    turtle.left(91)
    distance += 2
    
print('done!')
turtle.done()
