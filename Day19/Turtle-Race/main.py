from turtle import Turtle, Screen
from random import randint


is_race_on = False
screen = Screen()
screen.title("Turtle Race")
screen.setup(500, 400)
bet = screen.textinput(title="Make Your Bet", prompt="Who will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


def turtle(color, cords):
    new_turtles = Turtle(shape="turtle")
    new_turtles.color(color)
    new_turtles.penup()
    new_turtles.goto(cords)
    all_turtles.append(new_turtles)


current_cord = [-200, -110]
for _ in range(0, 6):
    turtle(color=colors[_],cords=current_cord)
    current_cord[1] += 50

if bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 225:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
