# q3_sol.py

"""
Using turtle graphics, draw three equilateral triangles with the
same center: a big one, a medium one inside the big one, and small
one inside the medium. See threeTriangles.gif for example output.

Hint: turtle.up() lifts the turtle pen up so it doesn't draw a line
when it moves. turtle.down() puts it back down.
"""
import turtle

# triangle 1
turtle.forward(300)
turtle.left(120)
turtle.forward(300)
turtle.left(120)
turtle.forward(300)
turtle.left(120)

# move turtle to the right and up
turtle.up()
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(25)
turtle.down()

# triangle 2
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)

# move turtle to the right and up
turtle.up()
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(25)
turtle.down()

# triangle 3
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)

turtle.done()
