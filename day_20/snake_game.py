from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# for segment_number in range(0, 3):
#     new_segment = Turtle()
#     new_segment.color("white")
#     new_segment.shape("square")
#     x = segment_number * -20
#     y = 0
#     new_segment.goto(x=x, y=y)
#     snake.append(new_segment)



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
