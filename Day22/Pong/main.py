from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # if you turn off the animation you have to manually update the screen

scoreboard = Scoreboard()
ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-320, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() > -320:
        ball.bounce(type="bounce")


    # Detect R paddle miss & L paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        ball.move_speed = 0.1

    if ball.xcor() < -340:
        ball.reset_position()
        scoreboard.r_point()
        SPEED = 0.1

screen.exitonclick()
