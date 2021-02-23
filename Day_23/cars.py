from turtle import Turtle
from random import randint
def random_color_generator():
    return(randint(0, 255), (randint(0, 255), (randint(0, 255)))) 

class Cars(Turtle):


    def __init__(self):
        super().__init__()
        self.color(random_color_generator())
        
        


