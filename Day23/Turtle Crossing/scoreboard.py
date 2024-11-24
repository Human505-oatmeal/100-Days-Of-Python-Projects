from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.level = 0
        self.write(f"Level {self.level}", font=FONT)

    def next_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", font=FONT)

    def game_over(self):
        game_over = Turtle()
        game_over.hideturtle()
        game_over.penup()
        game_over.goto(-70, 0)
        game_over.write("Game Over", font=FONT)


    # show level on the top left corner
    # after turtle is at FINISH_LINE_Y increment level (and make cars slightly faster)