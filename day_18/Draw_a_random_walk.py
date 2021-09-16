import random
from turtle import Turtle, Screen
from random import Random

tom = Turtle()
screen = Screen()
screen.colormode(255)

tom.speed(8)
tom.pensize(15)


def color_change():
    return random.randrange(0, 255, 10), random.randrange(0, 255, 10), random.randrange(0, 255, 10)


def walk():
    direction = random.randint(0, 1)
    angle = random.randrange(0, 360, 10)
    distance = 30
    # distance = random.randrange(10, 100, 10)
    tom.color(color_change())
    if direction == 0:
        tom.right(angle)
        tom.forward(distance)
    else:
        tom.left(angle)
        tom.forward(distance)


for _ in range(200):
    walk()

screen.exitonclick()
