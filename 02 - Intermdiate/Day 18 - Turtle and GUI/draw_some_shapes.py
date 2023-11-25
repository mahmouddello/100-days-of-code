import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()


def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    random_color = (R, G, B)
    return random_color


def drawShape(num_sides):
    change_color()
    angels = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angels)


for shape_size in range(3, 11):
    drawShape(shape_size)
    timmy.color(change_color())

screen = Screen()

screen.exitonclick()
