
from turtle import Turtle
# create list of co-ordinates for using tuples
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT_PACE = 20


class Snake:
    def __init__(self):
        self.starting_snake_body = []
        self.snake_instance()

    def snake_instance(self):
        # creates 3 snake instances using start_position
        for position in START_POSITION:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.starting_snake_body.append(snake)

    def movement(self):
        for snake_body in range(len(self.starting_snake_body) - 1, 0, -1):
            # Link the last 2 snake segment and reserve the head for[0]
            new_x = self.starting_snake_body[snake_body - 1].xcor()
            new_y = self.starting_snake_body[snake_body - 1].ycor()
            self.starting_snake_body[snake_body].goto(new_x, new_y)
        self.starting_snake_body[0].forward(MOVEMENT_PACE)
