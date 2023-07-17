import random
import turtle
from turtle import Turtle, Screen

etcher = Turtle()
turtle.colormode(255)


def move():
    etcher.forward(10)


def back():
    etcher.backward(10)


def turn_right():
    etcher.right(10)


def turn_left():
    etcher.left(10)


def clear():
    etcher.clear()
    etcher.penup()
    etcher.home()
    etcher.pendown()


screen = Screen()
screen.listen()
screen.onkey(key='w', fun=move)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='s', fun=back)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
