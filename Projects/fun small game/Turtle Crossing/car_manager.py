from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self,starting_position):
        super().__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.setheading(90)
        self.goto(starting_position)

    def car_move(self):
        go_to_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(go_to_x, self.ycor())

    def car_accelerator(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
