from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')


# TODO 5 : Create a Score board

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 270)  # Center & Top Alignment
        self.hideturtle()  # hides the turtle to show the text only
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER :(', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
