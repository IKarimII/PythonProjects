import turtle
from turtle import Turtle
import random

turtle.colormode(255)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
jeff = Turtle()
jeff.speed('fastest')
jeff.width(5)

ended = False
while not ended:
    rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    jeff.color(rgb)
    jeff.forward(20)
    jeff.setheading(random.choice(directions))
