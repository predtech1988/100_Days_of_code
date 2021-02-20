from turtle import Turtle


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.scores = 0
        self.new_scoreboard = Turtle()
        self.new_scoreboard.ht()
        self.new_scoreboard.penup()
        self.new_scoreboard.goto(x = 0, y =270)
        self.new_scoreboard.color("white")
        self.new_scoreboard.write(f"Score is: {self.scores}", False, "center", ("Arial", 16, "normal"))


    def add_score(self):        
        self.scores += 1
        self.new_scoreboard.clear()
        self.new_scoreboard.write(f"Score is: {self.scores}", False, "center", ("Arial", 16, "normal"))
        print(self.scores)
        self.new_scoreboard.ht()


    def game_over(self):
        self.new_scoreboard.goto(0, 0)
        self.new_scoreboard.write(f"GAME OVER!", False, "center", ("Arial", 16, "normal"))


