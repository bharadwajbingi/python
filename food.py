from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.speed('fastest')
        self.goto(randint(-280,280),randint(-280,280))
        self.shapesize(0.5)

    # def food_location(self):
    #     x = self.xcor()
    #     y = self.ycor()
    #     return x,y

    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280))