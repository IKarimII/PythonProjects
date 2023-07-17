from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.scored()

    def scored(self):
        self.score += 1
        self.clear()
        self.write(f"Level :{self.score}", font=("Courier", 24, "normal"), align='left')

    def you_lose(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=("Courier", 50, "normal"), align='center')
