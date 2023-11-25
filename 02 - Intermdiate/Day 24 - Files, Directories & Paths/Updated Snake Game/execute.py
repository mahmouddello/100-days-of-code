import time
from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.title('Snake Game')
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)  # Turning of the animation

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Right', fun=snake.right)
screen.onkey(key='Left', fun=snake.left)
game_is_on = True
while game_is_on:
    screen.update()
    scoreboard.update_scoreboard()
    time.sleep(0.1)
    snake.move()

    # TODO 4 : Detect collision with food
    if snake.head.distance(food) < 15:  # Snake's head colliding with the food\
        scoreboard.increase_score()
        snake.extend_body()
        food.refresh()  # Respawning new peace of food in a random coordinates

    # TODO 6 : Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    # TODO 7 : Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
