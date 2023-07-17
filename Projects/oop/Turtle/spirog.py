import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
jeff = Turtle()
jeff.speed('fastest')
jeff.width(2)


def draw_spiro(gap_size):
    for i in range(int(360 / gap_size)):
        rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        jeff.color(rgb)
        jeff.setheading(jeff.heading() + gap_size)
        jeff.circle(100)

draw_spiro(1)
screen = Screen()
screen.exitonclick()
