import time, os, random
from turtle import Turtle, Screen
from paddle import Paddle, Drawer
from ball import Ball, Scorer

window = Screen()
window.title('مضارب الكرة الذهبية')
window.bgcolor('black')
window.setup(width=1000, height=550)
window.tracer(0)

# رسام الحلبة
borderer = Drawer()
borderer.goto(-480,265)
borderer.pendown()
for i in range(2):
    borderer.forward(960)
    borderer.right(90)
    borderer.forward(530)
    borderer.right(90)

