from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_y, random_x = random.randint(-280, 280), random.randint(-280, 280)   # to keep away from the wall a bit
        self.goto(random_x, random_y)
