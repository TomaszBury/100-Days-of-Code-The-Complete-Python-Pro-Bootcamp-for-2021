from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food.
    if snake.head_of_the_snake.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall.
    if snake.head_of_the_snake.xcor() > 280 or snake.head_of_the_snake.ycor() < -280 or snake.head_of_the_snake.ycor() > 280 or snake.head_of_the_snake.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.snake[1::]:
        # if segment == snake.head_of_the_snake:
        #     pass
        if snake.head_of_the_snake.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    # if head collides with any segment in the tail:
        # trigger game_over

screen.exitonclick()
