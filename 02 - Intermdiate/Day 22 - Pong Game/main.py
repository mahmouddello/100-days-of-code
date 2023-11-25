import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

# Creating Screen
screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)  # turning off the animations

# Creating paddles and giving x and y coordinates through object's parameter (tuple)
right_paddle = Paddle(coordinates=(350, 0))
left_paddle = Paddle(coordinates=(-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()

# Moving controls for the right paddle
screen.onkey(key="Up", fun=right_paddle.go_up)
screen.onkey(key="Down", fun=right_paddle.go_down)

# Moving controls for the left paddle
screen.onkey(key="w", fun=left_paddle.go_up)
screen.onkey(key="s", fun=left_paddle.go_down)

# Updating the screen manually through a while loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # sleep for a little bit between each update
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect if the right_paddle miss
    if ball.xcor() > 380:
        scoreboard.left_point()
        ball.reset_position()

    # Detect if the left_paddle miss
    if ball.xcor() < -380:
        scoreboard.right_point()
        ball.reset_position()

    # Detect collision with right_paddle or left paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

# We detected the collision with paddle like this because distance method alone can't detect , it only measures the
# distance between the ball and the (center) of the paddle

screen.exitonclick()
