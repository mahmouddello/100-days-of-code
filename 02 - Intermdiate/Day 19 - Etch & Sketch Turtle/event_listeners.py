from turtle import Turtle, Screen

timmy = Turtle()


def move():
    timmy.forward(100)


screen = Screen()
screen.listen()
screen.onkey(key='w', fun=move)

screen.mainloop()
