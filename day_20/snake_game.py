from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# for segment_number in range(0, 3):
#     new_segment = Turtle()
#     new_segment.color("white")
#     new_segment.shape("square")
#     x = segment_number * -20
#     y = 0
#     new_segment.goto(x=x, y=y)
#     snake.append(new_segment)

for position in starting_positions:
    new_segment = Turtle()
    new_segment.penup()
    new_segment.color("white")
    new_segment.shape("square")
    new_segment.goto(position)
    snake.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for segment_number in range(len(snake) - 1, 0, -1):
        new_x = snake[segment_number - 1].xcor()
        new_y = snake[segment_number - 1].ycor()
        snake[segment_number].goto(new_x, new_y)

    snake[0].forward(20)

screen.exitonclick()
