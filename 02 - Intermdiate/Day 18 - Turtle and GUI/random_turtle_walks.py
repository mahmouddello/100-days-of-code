from turtle import Turtle, Screen
import random

directions = [0, 90, 180, 270]

myTurtle = Turtle()
myTurtle.speed(10)
myTurtle.pensize(5)


def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    random_color = (R, G, B)
    return random_color


for _ in range(100):
    myTurtle.forward(30)
    myTurtle.setheading(random.choice(directions))
    myTurtle.color(change_color())

screen = Screen()
screen.exitonclick()
