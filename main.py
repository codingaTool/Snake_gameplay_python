from turtle import Turtle, Screen
import time

screen = Screen()
screen.title("Snake Game")
screen.screensize(canvheight=600, canvwidth=600, bg="black")
screen.tracer(n=0)

# create list of co-ordinates for using tuples
start_position = [(0, 0), (-20, 0), (-40, 0)]
starting_snake_body = []

# creates 3 snake instances using start_position
for position in start_position:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(position)
    starting_snake_body.append(snake)


game_on = True
while game_on:
    screen.update()
    for snake_body in starting_snake_body:
        snake_body.forward(20)
        time.sleep(.1)


screen.exitonclick()
