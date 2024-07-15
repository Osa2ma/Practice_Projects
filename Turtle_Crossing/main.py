from turtle import *
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('white')
screen.title('Turtle Crossing Capstone')
screen.tracer(0)
player = Player()
car_manage = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,'Up')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manage.create_car()
    car_manage.move_cars()

    for car in car_manage.all_cars:
        if car.distance(player)<20:
            scoreboard.gameover()
            game_is_on = False
    
    if player.is_at_finish_line():
        player.go_to_start()
        car_manage.level_up()
        scoreboard.increase_level()



screen.exitonclick()
