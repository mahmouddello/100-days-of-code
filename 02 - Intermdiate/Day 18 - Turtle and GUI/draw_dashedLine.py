from turtle import Turtle, Screen

tt = Turtle()
for i in range(15):
    tt.forward(10)
    tt.penup()  # no drawing on moving
    tt.forward(10)
    tt.pendown()  # start drawing after moving

screen = Screen()
screen.exitonclick()
