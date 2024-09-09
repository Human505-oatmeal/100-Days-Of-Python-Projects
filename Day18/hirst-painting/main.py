import turtle
import colorgram
from random import choice
from turtle import Turtle, Screen

turtle.bgcolor("black")
turtle.colormode(255)
tim = Turtle()
tim.penup()
tim.speed(0)
tim.goto(x=-250, y=-200)
tim.hideturtle()
color_list = [(208, 160, 101), (150, 75, 37), (231, 213, 97), (245, 251, 247), (242, 247, 250), (132, 34, 21), (191, 156, 15), (87, 33, 21), (238, 174, 153), (21, 57, 80), (41, 117, 63), (31, 93, 135), (196, 98, 88), (2, 81, 115), (10, 99, 77), (194, 163, 165), (109, 159, 185), (73, 76, 40), (179, 209, 168), (106, 140, 129), (37, 27, 35), (78, 153, 168), (46, 50, 47), (134, 163, 150), (234, 178, 180), (2, 72, 136), (125, 64, 66), (118, 36, 39)]
x, y = -250, -200


for _ in range(10):
    tim.goto(x, y)
    y += 50
    for _ in range(10):
        tim.color(choice(color_list))
        tim.shape("circle")
        tim.stamp()
        tim.forward(50)

screen = turtle.Screen()
screen.exitonclick()
