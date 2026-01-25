from turtle import Turtle, Screen
import time, os, random

class Ball(Turtle):
  def __init__(self):
    super().__init__()
         self.shape('circle')
         self.color('white')
         self.penup()
         self.x_move = 10
         self.y_move = 10
        
        
class Scorer(Turtle):
        def __init__(self, position_given, shape = "classic", undobuffersize = 1000, visible = False):
             super().__init__(shape, undobuffersize, visible)
             self.penup()
             self.goto(position_given)
             self.score_left = 0
             self.score_right = 0
    
