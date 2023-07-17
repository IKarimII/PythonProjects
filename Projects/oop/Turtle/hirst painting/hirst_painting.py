import random
import turtle
from turtle import Turtle, Screen

colors = [(226, 226, 225), (236, 236, 239), (182, 65, 34), (213, 149, 97), (14, 24, 42), (230, 237, 233),
          (239, 208, 94), (241, 234, 238), (237, 62, 33), (157, 26, 19), (72, 29, 32), (84, 94, 115), (166, 141, 66),
          (67, 41, 35), (120, 32, 37), (183, 85, 94), (135, 152, 164), (49, 52, 127), (229, 175, 161), (165, 64, 70),
          (167, 141, 150), (98, 113, 112), (160, 168, 165), (189, 190, 196), (217, 174, 180), (15, 25, 24),
          (79, 70, 43), (183, 196, 189), (119, 121, 147), (248, 196, 4)]

dotter = Turtle()
turtle.colormode(255)
dotter.penup()
dotter.hideturtle()
dotter.speed('fastest')
y = -400

def dot_line(x, y):
    dotter.goto(x, y)
    for dots in range(10):
        dotter.dot(20, random.choice(colors))
        dotter.forward(50)

for i in range(10):
    y += 50
    dot_line(-400, y)


screen = Screen()
screen.exitonclick()
