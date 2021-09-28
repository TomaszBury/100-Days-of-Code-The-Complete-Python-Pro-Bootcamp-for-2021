from turtle import Turtle, Screen
import random

# tom = Turtle(shape="turtle")
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# tom.penup()
# tom.goto(x=-238, y=-100)

turtles = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    turtles.append(new_turtle)

for turtle in turtles:
    # if turtles.index(turtle) == 0:
    #     y = 0
    # elif turtles.index(turtle) % 2 == 0:
    #     y = (turtles.index(turtle) + 0) * 15
    # else:
    #     y = (turtles.index(turtle) + 1) * -15
    #     print(f"{y} & {turtles.index(turtle)} {0*-15}")

    if turtles.index(turtle) % 2 == 0:
        y = turtles.index(turtle) * 15
    else:
        y = (turtles.index(turtle) + 1) * -15
        # print(f"{y} & {turtles.index(turtle)}")
    turtle.goto(x=-238, y=y)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        if turtle.pencolor() == user_bet:
            random_distance += 1
        turtle.forward(random_distance)


screen.exitonclick()
