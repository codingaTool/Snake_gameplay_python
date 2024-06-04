from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time

screen = Screen()
screen.title("Snake Game")
screen.screensize(canvheight=600, canvwidth=600, bg="black")
screen.tracer(n=0)
screen.listen()

snake = Snake()
food = Food()
score = Scoreboard()

snake_head = snake.starting_snake_body[0]

screen.onkey(snake.up_control, "Up")
screen.onkey(snake.right_control, "Right")
screen.onkey(snake.down_control, "Down")
screen.onkey(snake.left_control, "Left")


game_on = True

while game_on:
    screen.update()
    time.sleep(.1)
    snake.movement()

    # check if snake collides with food and increase scoreboard
    if snake_head.distance(food) <20:
        food.refresh_food()
        score.increase_score()









screen.exitonclick()
