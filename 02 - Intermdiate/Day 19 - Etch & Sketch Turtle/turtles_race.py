import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
turtles = []
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
temp = 150
for x in range(0, 6):
    timmy = Turtle(shape='turtle')
    timmy.color(colors[x])
    timmy.penup()
    timmy.goto(x=-230, y=temp)
    temp -= 50
    turtles.append(timmy)

if not user_bet == "":
    is_race_on = True
winner_color = None
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if user_bet == winner_color:
                print(f'You Won, {winner_color} turtle wins the race')
                break
            else:
                print(f'You Lost, {winner_color} turtle wins the race')
        move = random.randint(0, 10)
        turtle.forward(move)
screen.exitonclick()
