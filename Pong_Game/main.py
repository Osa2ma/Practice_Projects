from turtle import *
import time
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width = 800,height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
pong_ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(right_paddle.up,'Up')
screen.onkeypress(right_paddle.down,'Down')
screen.onkeypress(left_paddle.up,'w')
screen.onkeypress(left_paddle.down,'s')

game_is_on=True
while game_is_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move()

    if pong_ball.ycor()>280 or pong_ball.ycor()<-280:
       pong_ball.bounce_y() 

    if (pong_ball.distance(right_paddle)<50 and pong_ball.xcor()>320) or (pong_ball.distance(left_paddle) < 50 and pong_ball.xcor()<-320):
        pong_ball.bounce_x()

    if pong_ball.xcor()>380:
        pong_ball.reset_position()
        scoreboard.l_point()
        

    if pong_ball.xcor()<-380:
        pong_ball.reset_position()
        scoreboard.r_point()
  

    
screen.exitonclick()
