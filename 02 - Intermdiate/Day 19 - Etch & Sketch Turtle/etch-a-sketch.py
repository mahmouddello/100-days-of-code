from turtle import Turtle, Screen

timmy = Turtle()


def forward():
    timmy.forward(10)


def backward():
    timmy.backward(10)


def clock_wise():
    timmy.right(90)


def counter_clock_wise():
    timmy.left(90)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen = Screen()
screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='d', fun=clock_wise)
screen.onkey(key='a', fun=counter_clock_wise)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
