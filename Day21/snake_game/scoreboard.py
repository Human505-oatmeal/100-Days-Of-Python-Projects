from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 240)
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_score()
