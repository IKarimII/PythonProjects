from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color("white")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        y_to = self.ycor() + 10
        self.goto(0, y_to)

    def move_down(self):
        y_to = self.ycor() - 10
        self.goto(0, y_to)

    def finish_line(self):
        self.goto(STARTING_POSITION)