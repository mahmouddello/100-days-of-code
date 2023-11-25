from turtle import Turtle, Screen
import random

timmy = Turtle()


def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    random_color = (R, G, B)
    return random_color


timmy.speed('fastest')


for x in range(100):
    timmy.circle(100)
    current_heading = timmy.heading()
    timmy.setheading(current_heading + 10)
    timmy.color(change_color())
screen = Screen()
screen.exitonclick()
