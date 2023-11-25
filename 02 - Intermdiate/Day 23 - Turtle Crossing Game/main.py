import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

# Creating and Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.bgcolor("white")
screen.tracer(0)

# Creating the Objects
player = Player()
score = ScoreBoard()
car_manager = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.move_up)

game_is_on = True

while game_is_on:
    screen.update()  # updating screen manually because we turned off the animations
    time.sleep(0.1)
    car_manager.create_cars()
    car_manager.move()
    # Detect car collision with the turtle then game is over
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False

    # Detect successful crossing
    if player.is_at_the_finish_line():
        score.level += 1
        score.update_scoreboard()
        player.next_level()
        car_manager.level_up()
        # Updates scoreboard, resets player position and speeds up the cars

screen.exitonclick()
