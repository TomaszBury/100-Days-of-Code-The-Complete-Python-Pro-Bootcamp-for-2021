import random
from turtle import Turtle, Screen
from random import Random

screen = Screen()
tom = Turtle()
screen.colormode(255)

for num_sides in range(3, 11):
    tom.color(random.randrange(0, 257, 10), random.randrange(0, 257, 10), random.randrange(0, 257, 10))
    angle = 360 / num_sides
    for _ in range(num_sides):
        tom.forward(100)
        tom.right(angle)

screen.exitonclick()

