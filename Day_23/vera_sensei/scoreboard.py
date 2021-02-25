from turtle import Turtle


FONT = ("Curier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.scores = 0
        self.ht()
        self.goto(y=230, x=-230)
        # self.write(f"Level: {self.scores}", False, "center", FONT)
    
    def add_score(self):
        self.scores += 1
        self.clear()
        self.write(f"Level: {self.scores}", False, "center", FONT)
