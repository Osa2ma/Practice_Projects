from turtle import *

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.goto(position)
        self.color('white')
        self.penup()

    def up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)

