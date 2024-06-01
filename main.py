from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.title("Snake Game")
screen.screensize(canvheight=600, canvwidth=600, bg="black")
screen.tracer(n=0)

snake = Snake()

game_on = True


while game_on:
    screen.update()
    time.sleep(.1)
    snake.movement()







screen.exitonclick()
