from turtle import Turtle, Screen
import random, os, time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10

class Scorer(Turtle):
    def __init__(self, color, position_assigned):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(color)
        self.goto(position_assigned)
        self.r_point = 0
        self.l_point = 0
    
    def add_score(self, determiner):
        self.clear()
        if determiner == 'left':
            self.l_point += 1
            self.write(f"{self.l_point}", font=('arial', 29, 'normal'))
        if determiner == 'right':
            self.r_point += 1
            self.write(f"{self.r_point}", font=('arial', 29, 'normal'))
        







