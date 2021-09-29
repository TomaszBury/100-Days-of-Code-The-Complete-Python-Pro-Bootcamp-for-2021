from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head_of_the_snake = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle()
            new_segment.penup()
            new_segment.color("white")
            new_segment.shape("square")
            new_segment.goto(position)
            self.snake.append(new_segment)

    def move(self):
        for segment_number in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment_number - 1].xcor()
            new_y = self.snake[segment_number - 1].ycor()
            self.snake[segment_number].goto(new_x, new_y)

        self.head_of_the_snake.forward(MOVE_DISTANCE)

    def up(self):
        if self.head_of_the_snake.heading() != DOWN:
            self.head_of_the_snake.setheading(UP)

    def down(self):
        if self.head_of_the_snake.heading() != UP:
            self.head_of_the_snake.setheading(DOWN)

    def left(self):
        if self.head_of_the_snake.heading() != RIGHT:
            self.head_of_the_snake.setheading(LEFT)

    def right(self):
        if self.head_of_the_snake.heading() != LEFT:
            self.head_of_the_snake.setheading(RIGHT)
