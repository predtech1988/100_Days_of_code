from turtle import Turtle

class Pad(Turtle):
    def __init__(self, coordinates):
        """
        takes tuple for coordinates (x, y)
        """
        super().__init__()
        self.current_score = 0
        self.penup()
        self.goto(coordinates)
        self.shape("square")
        self.setheading(90)
        self.color("white")
        self.shapesize(stretch_wid= 1, stretch_len= 5)
        #print(self.shapesize())


    def move_up(self):
        if self.ycor() <= 225:
            self.forward(45)
            #print(self.ycor())


    def move_down(self):
        if self.ycor() >= -225:
            self.backward(45)
            #print(self.ycor())
        