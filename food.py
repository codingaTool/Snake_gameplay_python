from turtle import Turtle
import random
RANDOM_XCORD = random.randint(-270, 270)
RANDOM_YCORD = random.randint(-270, 270)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.9, stretch_wid=0.9)
        self.color("green")
        self.speed("fastest")
        self.goto(x=RANDOM_XCORD,y=RANDOM_YCORD)

# print(RANDOM_XCORD)
# print(RANDOM_YCORD)