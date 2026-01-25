from turtle import Turtle, Screen
import time, os, random

class Paddle(Turtle):
    def __init__(self, position__to, color):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color(color)
        self.goto(position__to)
        self.shapesize(stretch_len=1, stretch_wid=5)
    
    def go_up(self):
        self.goto(self.xcor(), self.ycor()+100)

    def go_down(self):
        self.goto(self.xcor(), self.ycor()-100)

class Drawer(Turtle):
    def __init__(self):
        super().__init__()
        self.color('orange')
        self.penup()
        self.hideturtle()
        self.pensize(10)
        self.speed('fastest')
