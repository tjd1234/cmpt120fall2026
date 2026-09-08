# spiral2_sol.py

import turtle

turtle.setup(startx=10, starty=10)
turtle.speed(0)

max_X = turtle.window_width() / 2
min_X = -max_X
max_Y = turtle.window_height() / 2
min_Y = -max_Y

def off_screen(turtle):
    x, y = turtle.position()
    return x > max_X or x < min_X or y > max_Y or y < min_Y

#
# Re-write this so that the loop ends when the turtle is off the screen.
#
distance = 1
while not off_screen(turtle):
    turtle.forward(distance)
    turtle.left(91)
    distance += 2
    
print('done!')
turtle.done()
