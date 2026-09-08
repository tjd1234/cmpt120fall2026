# circles.py

import turtle

# def draw_circles():
#     turtle.circle(100)
#     turtle.circle(75)
#     turtle.circle(50)
#     turtle.circle(25)

def draw_circles(start_radius):
    turtle.begin_fill()
    turtle.circle(start_radius)
    turtle.end_fill()

    turtle.color("green")
    turtle.begin_fill() 
    turtle.circle(start_radius - 25)
    turtle.end_fill()

    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(start_radius - 50)
    turtle.end_fill()

    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(start_radius - 75)
    turtle.end_fill()

draw_circles(5)
turtle.done()
