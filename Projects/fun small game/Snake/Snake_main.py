from turtle import Screen
from Scoreboard import ScoreBoard
from Snake import Snake
from Food import Food

snape = Snake()
score_board = ScoreBoard()
screen = Screen()
food = Food()

screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake ~ Made by Karim')
screen.tracer(0)

screen.listen()
screen.onkey(snape.up, key="w")
screen.onkey(snape.down, key="s")
screen.onkey(snape.left, key="a")
screen.onkey(snape.right, key="d")

game_is_on = True

while game_is_on:
    screen.update()

    snape.move_block()
    if snape.head.distance(food) < 20:
        snape.extend()
        score_board.score_display()
        food.random_location()

    if snape.head.xcor() > 290 or snape.head.xcor() < -295 or snape.head.ycor() > 295 or snape.head.ycor() < -290:
        snape.restart()
        score_board.game_over()

    for segment in snape.block[1:]:
        if snape.head.distance(segment) < 10:
            snape.restart()
            score_board.game_over()


screen.exitonclick()
