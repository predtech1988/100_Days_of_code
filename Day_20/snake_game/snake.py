from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:

    def __init__(self, number):
        self.turtles_list = []
        self.new_segment(number)

    def new_segment(self, num):
        for i in range(num):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()            
            new_turtle.goto(x=len(self.turtles_list)*(-20), y=0)            
            self.turtles_list.append(new_turtle)

    def move(self):
        for turtle in range(len(self.turtles_list)-1, 0, -1):
            new_x = self.turtles_list[turtle - 1].xcor()
            new_y = self.turtles_list[turtle - 1].ycor()
            self.turtles_list[turtle].goto(new_x, new_y)
        self.turtles_list[0].forward(MOVE_DISTANCE)

    def reset(self):
        for segment in self.turtles_list:
            segment.goto(1000, 1000)
        self.turtles_list.clear()
        self.new_segment(3)

    def up(self):
        if self.turtles_list[0].heading() != 270:
            self.turtles_list[0].seth(90)

    def down(self):
        if self.turtles_list[0].heading() != 90:
            self.turtles_list[0].seth(270)

    def left(self):
        if self.turtles_list[0].heading() != 0:
            self.turtles_list[0].seth(180)

    def right(self):
        if self.turtles_list[0].heading() != 180:
            self.turtles_list[0].seth(0)
