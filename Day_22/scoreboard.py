from turtle import Turtle


class Scoreboard(Turtle):
    
    #def __init__(self):
        # super().__init__()
        # self.scores = 0        
        # self.color ="white"
        # self.penup()
        # self.goto(0, 0)
        # self.write(f"Score is: {self.scores}", False, "center", ("Arial", 16, "normal"))

    def __init__(self, l_pad, r_pad):
        super().__init__()
        self.scores = 0
        self.ht()
        self.penup()
        self.goto(x = 0, y = 250)
        self.shape("square")

        self.setheading(90)
        self.color("white")
        
        self.write(f"{l_pad.current_score} : {r_pad.current_score}", False, "center", ("Terminal", 24, "normal"))
        print(self.shapesize())



    def update_scores(self, l_pad, r_pad):
        self.clear()
        self.write(f"{l_pad.current_score} : {r_pad.current_score}", False, "center", ("Terminal", 24, "normal"))
        

    def game_over(self):
        self.clear()
        self.goto(x = 0, y =0)
        self.write(f"GAME OVER", False, "center", ("Terminal", 24, "normal"))
        