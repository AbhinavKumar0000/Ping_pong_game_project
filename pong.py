from turtle import Turtle
from turtle import Screen
screen = Screen()

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() > 220:
            pass
        else:
            y_new = self.ycor() + 20
            self.goto(self.xcor(), y_new)


    def go_down(self):
        if self.ycor() < -220:
            pass
        else:
            y_new = self.ycor() - 20
            self.goto(self.xcor(), y_new)

