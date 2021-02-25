from turtle import Turtle, Screen
import time
from cars import Cars
from random import randint
screen = Screen()
screen.colormode(255)
cars_list = []
def car_generator():
    for i in range(5):
        random_car = Cars()
        cars_list.append(random_car)

car_generator()
print(cars_list)

