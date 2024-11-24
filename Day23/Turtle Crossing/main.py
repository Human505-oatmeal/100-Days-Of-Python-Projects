import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
screen = Screen()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.finish_line():
        player.go_to_start()
        scoreboard.next_level()

    # if player.ycor() >= 260:
    #     scoreboard.game_over()
    car_manager.create_car()
    car_manager.move_car()

    # Detect turtle collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()