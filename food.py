from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("green")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        RANDOM_XCORD = random.randint(-270, 270)
        RANDOM_YCORD = random.randint(-270, 270)
        self.goto(x=RANDOM_XCORD,y=RANDOM_YCORD)
        print("nom nom")


# print(RANDOM_XCORD)
# print(RANDOM_YCORD)