import random
from turtle import Turtle

COLORS = ["green", "blue", "red", "yellow", "orange", "purple", "pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []  # list to hold all cars
        self.car_speed = STARTING_MOVE_DISTANCE  # car speed

    def create_cars(self):
        random_chance = random.randint(1, 6)  # reducing the chances to create too many cars
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(x=300, y=random_y)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT  # increases car speed by MOVE_INCREMENT amount
