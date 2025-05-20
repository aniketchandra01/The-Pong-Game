import time
from turtle import *
from paddles import Paddles
from net import Net

screen = Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.listen()

paddles = Paddles()
net = Net()
print(net.shapetransform())
screen.update()

screen.onkeypress(paddles.right_up_pressed, "Up")
screen.onkeypress(paddles.right_down_pressed, "Down")
screen.onkeypress(paddles.left_up_pressed,"w")
screen.onkeypress(paddles.left_down_pressed,"s")
screen.onkeyrelease(paddles.right_up_released, "Up")
screen.onkeyrelease(paddles.right_down_released, "Down")
screen.onkeyrelease(paddles.left_up_released, "w")
screen.onkeyrelease(paddles.left_down_released, "s")

while True:

    paddles.movement()
    screen.update()
    time.sleep(0.02)

screen.exitonclick()


