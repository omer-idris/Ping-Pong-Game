import os, random, time, string
from turtle import Turtle, Screen
from new_paddle import Paddle 
from new_ball import Ball, Scorer

window = Screen()
window.title('مضارب الكرة الذهبية')
window.bgcolor('black')
window.setup(width=1000, height=550)
window.tracer(0)



# رسام الحلبة
borderer = Turtle()
borderer.penup()
borderer.color('orange')
borderer.pensize(9)
borderer.goto(-480,265)
borderer.pendown()
for i in range(2):
    borderer.forward(960)
    borderer.right(90)
    borderer.forward(530)
    borderer.right(90)
borderer.hideturtle()
borderer.penup()
borderer.goto(0,260)

# رسم الشبكة في المنتصف
borderer.right(90)
for i in range(14):
    borderer.pendown()
    borderer.forward(53/3)
    borderer.penup()
    borderer.forward(63/3)

ball = Ball()

right_paddle = Paddle(position_to=(450,0), color='cornflowerblue')
left_paddle =  Paddle(position_to=(-450,0), color='red')

window.listen()
window.onkey(right_paddle.go_up,'j')
window.onkey(right_paddle.go_down,';')
window.onkey(left_paddle.go_up,'f')
window.onkey(left_paddle.go_down,'a')

right_score =  Scorer(color='cornflowerblue', position_assigned=(200,200))
left_score =  Scorer(color='red', position_assigned=(-200,200))

default_time = 0.02
def Ping_Pong():
    global default_time
    on_go = True
    while on_go:
        window.update()
        time.sleep(default_time)

        # اضف قيمة الموڨــ (مقدرا الحركة) على كل محور من الإكس والواي واذهب اليها
        ball.goto(ball.xcor() + ball.x_move, ball.ycor() + ball.y_move)

        # الإصطدام مع الأعلى أو الأسفل
        if ball.ycor() >= 250 or ball.ycor() <= -250:
            ball.y_move *= -1

        # الإصطدام مع المضارب
        if (ball.xcor() >= 450 and ball.distance(right_paddle) <= 50) or (ball.xcor() <= -450 and ball.distance(left_paddle) <= 50):
            ball.x_move *= -1
            default_time *= 0.8
        
        # الافلات من الأيمن واضافة درجة للأيسر
        if ball.xcor() > 550:
            ball.goto(0,0)
            default_time = 0.02
            ball.x_move *= -1
            left_score.add_score('left')

        # الافلات من الأيسر واضافة درجة للأيمن
        if ball.xcor() < -550:
            ball.goto(0,0)
            default_time = 0.02
            ball.x_move *= -1
            right_score.add_score('right')

Ping_Pong()

window.exitonclick()
