import random, os, time
from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, position_to, color, shape='square'):
        super().__init__(shape)
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(position_to)
        self.color(color)
        self.speed('fastest')
    
    def go_up(self):
        self.goto(self.xcor(), self.ycor()+100)

    def go_down(self):
        self.goto(self.xcor(), self.ycor()-100)
