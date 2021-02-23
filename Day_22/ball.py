from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.moving_y = 10
        self.moving_x = 10


    def ball_move(self):
        self.new_x = self.xcor() + self.moving_x
        self.new_y = self.ycor() + self.moving_y
        self.goto(self.new_x, self.new_y)

    def ball_bounce_y(self):
        self.moving_y *= -1

    def ball_bounce_x(self):
        self.moving_x *= -1


    #Trash :(
    # def ball_move(self, direction):
    #     self.moving_speed = 20
    #     if direction == "up_r":
    #         self.new_x = self.xcor() + self.moving_speed
    #         self.new_y = self.ycor() + self.moving_speed
    #         self.goto(self.new_x, self.new_y)
        
    #     elif direction == "up_l":
    #         self.new_x = self.xcor() - self.moving_speed
    #         self.new_y = self.ycor() + self.moving_speed
    #         self.goto(self.new_x, self.new_y)

    #     elif direction == "down_r":
    #         self.new_x = self.xcor() + self.moving_speed
    #         self.new_y = self.ycor() - self.moving_speed
    #         self.goto(self.new_x, self.new_y)

    #     elif direction == "down_l":
    #         self.new_x = self.xcor() - self.moving_speed
    #         self.new_y = self.ycor() - self.moving_speed
    #         self.goto(self.new_x, self.new_y)
        
    #     elif direction == "left":
    #         self.new_x = self.xcor() - self.moving_speed
    #         self.new_y = self.ycor() - self.moving_speed
    #         self.goto(self.new_x, self.new_y)
        
    #     elif direction == "right":
    #         self.new_x = self.xcor() + self.moving_speed
    #         self.new_y = self.ycor() + self.moving_speed
    #         self.goto(self.new_x, self.new_y)
    #     else:
    #         print("Something wrong, ball/py line 23")



        # self.moving_speed = 1
        # self.x_limit = 300
        # self.y_limit = 400
        # self.x_cor = 0
        # self.y_cor = 0
        # while self.x_cor < self.x_limit or self.y_cor < self.y_limit:
        #     self.x_cor += self.moving_speed
        #     self.y_cor += self.moving_speed
        #     self.goto(self.x_cor, self.y_cor)



    def ball_curren_position(self):
        print(self.ycor())
