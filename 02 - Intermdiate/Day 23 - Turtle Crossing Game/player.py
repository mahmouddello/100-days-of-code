from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE = 10
FINISH = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        new_position = self.ycor() + MOVE
        self.goto(self.xcor(), new_position)

        # OR:  self.forward(MOVE)

    def is_at_the_finish_line(self):
        if self.ycor() > FINISH:
            return True
        else:
            return False
        # Checks if the player reached the finish line

    def next_level(self):
        self.goto(STARTING_POSITION)  # resets the position of the player for the next level
