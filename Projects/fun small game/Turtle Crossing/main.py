import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

lil_turt = Player()
screen.listen()
screen.onkeypress(lil_turt.move_up, 'w')
screen.onkeypress(lil_turt.move_down, 's')

cars = []
times = 50

score_board = Scoreboard()


def add_cars():
        starting_position = (random.randint(200, 300), random.randint(-250, 260))
        car = CarManager(starting_position)
        cars.append(car)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    times += 1

    for car in cars:
        if lil_turt.distance(car) < 30 and lil_turt.ycor() >= car.ycor() - 20:
            score_board.you_lose()
            game_is_on = False

    if times >= 6:
        times = 0
        add_cars()

    for car in cars:
        car.car_move()

    if lil_turt.ycor() > 280:
        score_board.scored()
        car.car_accelerator()
        lil_turt.finish_line()
        for car in cars:
            car.goto(-500, 500)

screen.exitonclick()
