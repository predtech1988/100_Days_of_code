from turtle import Turtle


class Wall(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        #self.ht()
        self.penup()
        self.goto(coordinates)
        self.shape("square")
        self.setheading(90)
        self.color("red")
        self.shapesize(stretch_wid= 30, stretch_len= 0.5)


