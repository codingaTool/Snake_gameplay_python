from turtle import Turtle, Screen

screen = Screen()
screen.title("Snake Game")
screen.screensize(canvheight=600, canvwidth=600, bg="black")

# create list of co-ordinates for using tuples
start_position = [(0, 0), (-20, 0), (-40, 0)]

for position in start_position:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.goto(position)
    print(position)

screen.listen()
screen.exitonclick()
