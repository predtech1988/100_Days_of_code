from turtle import Turtle
from random import randint
import time

def random_color_generator():
    return(randint(0, 255)), (randint(0, 255)), (randint(0, 255))

def  random_positions():
    x_pos = randint(-20, 9900)
    y_pos = randint(-260, 280)

    while not (y_pos % 20) == 0:
        y_pos = randint(-240, 260)        
    return x_pos, y_pos
 

class Cars(Turtle):

    def __init__(self):
        super().__init__()   
        self.color(random_color_generator())
        self.penup()
        self.shape("square")
        self.setheading(180)
        self.shapesize(1, 2)
        self.car_moving_speed = 5
        self.goto(random_positions())
        
    def move_car(self):
        self.fd(self.car_moving_speed)
        

        



