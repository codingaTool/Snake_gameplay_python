from score_board import Scoreboard
from turtle import Turtle
# create list of co-ordinates for using tuples
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT_PACE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.starting_snake_body = []
        self.snake_instance()

    def snake_instance(self):
        # creates 3 snake instances using start_position
        for position in START_POSITION:
            self.snake_segments(position)

    def snake_segments(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.starting_snake_body.append(snake)

    def snake_grow(self):
        self.snake_segments(self.starting_snake_body[-1].position())

    def movement(self):
        for snake_body in range(len(self.starting_snake_body) - 1, 0, -1):
            # Link the last 2 snake segment and reserve the head for[0]
            new_x = self.starting_snake_body[snake_body - 1].xcor()
            new_y = self.starting_snake_body[snake_body - 1].ycor()
            self.starting_snake_body[snake_body].goto(new_x, new_y)
        self.starting_snake_body[0].forward(MOVEMENT_PACE)

    def up_control(self):
        if self.starting_snake_body[0].heading() != DOWN: # If the snake head is going Up, its not allowed to go down
            self.starting_snake_body[0].setheading(UP)

    def right_control(self):
        if self.starting_snake_body[0].heading() != LEFT:
            self.starting_snake_body[0].setheading(RIGHT)

    def down_control(self):
        if self.starting_snake_body[0].heading() != UP:
            self.starting_snake_body[0].setheading(DOWN)

    def left_control(self):

        if self.starting_snake_body[0].heading() != RIGHT:
            self.starting_snake_body[0].setheading(LEFT)