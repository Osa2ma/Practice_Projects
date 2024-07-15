from turtle import *
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

mysnake = Snake()
myfood=Food()
myscore=Scoreboard()
screen.listen()
screen.onkey(mysnake.up,"Up")
screen.onkey(mysnake.down,"Down")
screen.onkey(mysnake.left,"Left")
screen.onkey(mysnake.right,"Right")
game_is_on = True

# Game loop
while game_is_on:
    screen.update()
    time.sleep(0.1)
    mysnake.move()

    if mysnake.head.distance(myfood) < 15:
        myfood.refresh()
        mysnake.extend()
        myscore.score +=1
        myscore.update_scoreboard()

    if mysnake.head.xcor()>280 or mysnake.head.xcor()<-280 or mysnake.head.ycor()>280 or mysnake.head.ycor() < -280:
        myscore.reset()
        mysnake.reset()
        

    for segment in mysnake.segments[1:]:
        
        if mysnake.head.distance(segment)<10:
            myscore.reset()
            mysnake.reset()
            
            





screen.exitonclick()
