from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.appear()

    def appear(self):
        position_x = random.randint(-380, 380)
        position_y = random.randint(-380, 380)
        self.goto(position_x, position_y)
