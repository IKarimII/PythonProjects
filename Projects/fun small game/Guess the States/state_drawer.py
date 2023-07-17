from turtle import Turtle


class state_drawer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')

    def state_draw(self, state, x, y):
        self.goto(x, y)
        self.write(f"{state}", font=("Arial", 20, 'normal'), align='center')


