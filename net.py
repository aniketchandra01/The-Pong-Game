from turtle import *

class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.teleport(0,270)
        self.setheading(270)
        self.pensize(10)


        self.create()

    def create(self):
        for x in range(0,8):
            self.forward(40)
            self.penup()
            self.forward(30)
            self.pendown()



