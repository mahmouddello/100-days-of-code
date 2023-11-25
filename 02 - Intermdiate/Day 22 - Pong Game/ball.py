from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_x(self):
        self.x_move *= -1  # when the ball bounce if the x is positive it's going to be negative and vice-versa
        self.move_speed *= 0.9
        self.speed(self.move_speed)

    def bounce_y(self):
        self.y_move *= -1  # when the ball bounce if the y is positive it's going to be negative and vice-versa

    def reset_position(self):
        self.setposition(x=0, y=0)
        self.bounce_x()  # when the ball is missed by a player, it reverses it direction in the next round
