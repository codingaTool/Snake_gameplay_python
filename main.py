from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.title("Snake Game")
screen.screensize(canvheight=600, canvwidth=600, bg="black")
screen.tracer(n=0)
screen.listen()

snake = Snake()
food = Food()

screen.onkey(snake.up_control, "Up")
screen.onkey(snake.right_control, "Right")
screen.onkey(snake.down_control, "Down")
screen.onkey(snake.left_control, "Left")


game_on = True

while game_on:
    screen.update()
    time.sleep(.09)
    snake.movement()







screen.exitonclick()
