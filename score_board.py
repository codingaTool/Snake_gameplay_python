from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(x=0, y=320)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align= "center", font=("courier", 24, "normal"))

    def game_over(self):
        self.color("red")
        self.goto(x=0, y=200)
        self.write(f"GAME OVER...Try Again", align= "center", font=("courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


