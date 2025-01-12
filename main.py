from turtle import Screen, Turtle
import time
from pong import Paddle
from ball import Ball
from  scorebaord import Scoreboard
screen = Screen()
ball = Ball()
scoreboard = Scoreboard()

screen.title("Pong game")
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))





screen.listen()
screen.onkeypress(key="Up",fun = paddle_r.go_up)
screen.onkeypress(key = "Down", fun = paddle_r.go_down)
screen.onkeypress(key="w",fun = paddle_l.go_up)
screen.onkeypress(key = "s", fun = paddle_l.go_down)

# mid part
kachua = Turtle()
kachua1 = Turtle()
for _ in range(15):

    kachua.setheading(90)
    kachua.forward(10)
    kachua.color("white")
    kachua.forward(10)
    kachua.color("black")

for _ in range(15):
    kachua1.setheading(270)
    kachua1.forward(10)
    kachua1.color("white")
    kachua1.forward(10)
    kachua1.color("black")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #colision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    if ball.distance(paddle_l) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    #detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()












screen.exitonclick()