from turtle import *
shape("turtle")
speed(2)


def make_triangle():
    for i in range(3):
        left(120)
        forward(50)


def make_polygon(n_sides):
    for i in range(n_sides):
        forward(50 + (3 * n_sides))
        left(360 / n_sides)


def make_shape(n):
    left(30)
    make_triangle()
    right(30)
    penup()
    forward(10)
    pendown()
    left(135)
    for i in range(4, n):
        make_polygon(i)
        right(90 + (180 / i))
        penup()
        forward(10)
        pendown()
        left(90 + (180 / (i + 1)))


make_shape(int(input("Number of Polygons to Draw by Turtle: ")))
done()