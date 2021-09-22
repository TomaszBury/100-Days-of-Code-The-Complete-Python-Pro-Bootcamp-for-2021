import random
from turtle import Turtle, Screen
import colorgram

tom = Turtle()
screen = Screen()
screen.colormode(255)

# Extract 6 colors from an image.
colors = colorgram.extract('danmien_hirst_complete_sport.jpg', 15)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb  # e.g. (255, 151, 210)

tom.pensize(15)
tom.penup()
tom.left(180)
tom.forward(400)
tom.right(270)
tom.forward(400)
tom.left(90)
tom.pendown()

number_of_lines = 40
length_of_color = 1
length_of_blank = 20


# tom.forward(100)
# tom.right(180)
# tom.forward(250)
# tom.left(90)
# tom.forward(300)
# tom.left(90)

def move_to_new_line():
    tom.penup()
    tom.left(90)
    tom.forward(2 * 10)
    tom.left(90)
    tom.forward(number_of_lines * (length_of_color + length_of_blank))
    tom.right(180)
    tom.pendown()


def random_color():
    return random.choice(colors).rgb


def paint_new_line():
    for _ in range(0, number_of_lines):
        tom.color(random_color())
        tom.forward(length_of_color)
        tom.penup()
        tom.forward(length_of_blank)
        tom.pendown()


for _ in range(0, number_of_lines):
    paint_new_line()
    move_to_new_line()

screen.exitonclick()
