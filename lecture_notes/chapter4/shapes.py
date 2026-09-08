# shapes.py

import turtle

def square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)

def triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)

def star(length):
    for i in range(5):
        turtle.forward(length)
        turtle.right(144)

def flower(length, shape_func):
    for i in range(10):
        shape_func(length)
        turtle.right(36)

def pattern1():
    square(100)
    triangle(100)
    star(100)
    turtle.hideturtle()

def pattern2():
    for i in range(10):
        star(100)
        turtle.right(36)
    turtle.hideturtle()

def pattern3():
    for i in range(12):
        star(100)
        turtle.right(30)
    turtle.hideturtle()

# put the turtle window in a more convenient location
turtle.Screen().setup(startx=900, starty=0)

# flower(100, star)

# pattern1()
# pattern2()
pattern3()

turtle.done()
