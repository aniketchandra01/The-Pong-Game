import time
from turtle import *

positions = [(-390,0),(380,0)]

class Paddles:
    def __init__(self):
        self.paddles = []

        for position in positions:
            paddle = Turtle()
            paddle.setheading(90)
            paddle.penup()
            paddle.color('white')
            paddle.teleport(position[0], position[1])
            paddle.shape('square')
            paddle.shapetransform(1, 0, 0, 5)
            self.paddles.append(paddle)

        self.right_moving_up = False
        self.right_moving_down = False
        self.left_moving_up = False
        self.left_moving_down = False

        self.left = self.paddles[0]
        self.right = self.paddles[1]


    def movement(self):
        if self.left_moving_up:
            if self.left.ycor() < 245:
                self.left.forward(10)
        elif self.left_moving_down:
            if self.left.ycor() >= -230:
                self.left.backward(10)

        if self.right_moving_up:
            if self.right.ycor() < 245:
                self.right.forward(10)
        elif self.right_moving_down:
            if self.right.ycor() >= -230:
                self.right.backward(10)




    def right_up_pressed(self):
        self.right_moving_up = True

    def left_up_pressed(self):
        self.left_moving_up = True

    def right_down_pressed(self):
        self.right_moving_down = True

    def left_down_pressed(self):
        self.left_moving_down = True

    def right_up_released(self):
        self.right_moving_up = False

    def left_up_released(self):
        self.left_moving_up = False

    def right_down_released(self):
        self.right_moving_down = False

    def left_down_released(self):
        self.left_moving_down = False



