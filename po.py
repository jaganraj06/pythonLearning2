import turtle


win = turtle.Screen()
win.setup(width=800,height=600)
win.bgcolor("green")
win.title("Pong Game")
win.tracer(0)

win = turtle.Screen()
win.setup(width=800,height=600)
win.bgcolor("green")
win.title("Pong Game")


#left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("blue")
left_paddle.shapesize(stretch_len=1,stretch_wid=5)

left_paddle.goto(-380,0)

#rightpaddle
right_paddle = turtle.Turtle()
right_paddle.speed(10)
right_paddle.shape("square")
right_paddle.color("blue")
right_paddle.shapesize(stretch_len=1,stretch_wid=5)
right_paddle.penup()
right_paddle.goto(380,0)




while True:
    win.update()
