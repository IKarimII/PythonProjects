from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.block = []
        self.starting_blocks()
        self.head = self.block[0]

    def starting_blocks(self):
        for position in STARTING_POSITIONS:
            self.new_block(position)

    def new_block(self, position):
        new_block = Turtle('square')
        new_block.color('white')
        new_block.penup()
        new_block.goto(position)
        self.block.append(new_block)

    def extend(self):
        x = self.block[-1].xcor()
        y = self.block[-1].ycor()
        self.new_block((x, y))

    def move_block(self):
        for i in range(len(self.block) - 1, 0, -1):
            x = self.block[i - 1].xcor()
            y = self.block[i - 1].ycor()
            self.block[i].goto(x, y)
        self.head.forward(MOVE_DISTANCE)
        time.sleep(0.1)

    def restart(self):
        for block in self.block:
            block.goto(1000,1000)
        self.block.clear()
        self.starting_blocks()
        self.head = self.block[0]
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
