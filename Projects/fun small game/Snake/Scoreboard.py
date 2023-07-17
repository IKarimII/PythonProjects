import time
from turtle import Turtle

ALIGNMENT = 'center'
Font = ("Arial", 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", mode='r') as file:
            self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.score_display()

    def score_display(self):
        self.goto(0, 260)
        self.clear()
        self.write(f"Score : {self.score} HighScore : {self.high_score}", align=ALIGNMENT, font=Font)
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=Font)
        time.sleep(0.5)
        with open('data.txt', mode='w') as file:
            file.write(str(self.high_score))

        self.play_again()

    def play_again(self):
        self.score = 0
        self.score_display()

