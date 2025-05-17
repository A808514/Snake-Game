from turtle import Turtle

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(0 , 350)