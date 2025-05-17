from turtle import Turtle
import random

shapes = ["circle", "triangle", "square", "turtle"]
colors = ["red", "green", "blue", "yellow", "purple", "white"]

size = random.uniform(1, 4)


class Shapes(Turtle):
    def __init__(self):
        super().__init__()
        random_shape = random.choice(shapes)
        self.shape(random_shape)
        self.color(random.choice(colors))
        self.penup()
        self.shapesize(stretch_wid=size, stretch_len=size)
        self.goto(random.randint(-460, 460), 500)

    def move_shapes(self):
        self.goto(self.xcor(), self.ycor() - 10)
