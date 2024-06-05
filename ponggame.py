import turtle
import winsound

score_a = 0
score_b = 0

win = turtle.Screen()
win.setup(width=800,height=600)
win.bgcolor("green")
win.title("Pong Game")
win.tracer(0)

#left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("blue")
left_paddle.shapesize(stretch_len=1,stretch_wid=5)
left_paddle.penup()
left_paddle.goto(-380,0)

#rightpaddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("blue")
right_paddle.shapesize(stretch_len=1,stretch_wid=5)
right_paddle.penup()
right_paddle.goto(380,0)


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.dx = 0.15
ball.dy = 0.15

#score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center",font =("Ariel",24,"normal"))

#moveingpaddles
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor()+20)
def left_paddle_down():
    left_paddle.sety(left_paddle.ycor()-20)
def right_paddle_up():
    right_paddle.sety(right_paddle.ycor()+20)
def right_paddle_down():
    right_paddle.sety(right_paddle.ycor()-20)


win.listen()
win.onkeypress(left_paddle_up,'w')
win.onkeypress(left_paddle_down,'s')
win.onkeypress(right_paddle_up,'Up')
win.onkeypress(right_paddle_down,'Down')





while True:
    win.update()
    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #ball-wall collision
    #top wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    #bottom wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    #right wall
    if ball.xcor()  > 390:
        ball.setx(390)
        ball.dx *= -1
    #left wall
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    #collision with paddles
    if ball.xcor() > 370 and right_paddle.ycor()-50 < ball.ycor()<right_paddle.ycor()-50:
        ball.setx(360)
        ball.dx *= -1
    if ball.xcor() < -370 and left_paddle.ycor()-50 < ball.ycor()<left_paddle.ycor()-50:
        ball.setx(-360)
        ball.dx *= -1









