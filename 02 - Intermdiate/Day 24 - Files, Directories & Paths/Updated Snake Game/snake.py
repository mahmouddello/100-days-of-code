from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # TODO 1 : Create the Snake's Body
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # Snake's head segment

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend_body(self):
        self.add_segment(self.segments[-2].position())

    # TODO 2 : Move the Snake
    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_segment_position = self.segments[segment_number - 1].position()
            self.segments[segment_number].goto(new_segment_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)  # Makes the old snake disappear from the screen
        self.segments.clear()  # Removes all segments from the list
        self.create_snake()
        self.head = self.segments[0]
