from turtle import Turtle, Screen

t = Turtle()  # Turtle object

t.shape('turtle')  # Appearance in the screen
t.color('red')  # changing the color of the turtle on the screen

# Motion and Drawing:
t.forward(100)
t.right(90)  # Turning Right (South)

screen = Screen()
screen.exitonclick()
