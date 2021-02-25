from turtle import Turtle


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.scores = 0
        self.highscore = self.read_highscore()
        self.new_scoreboard = Turtle()
        self.new_scoreboard.ht()
        self.new_scoreboard.penup()
        self.new_scoreboard.goto(x = 0, y =270)
        self.new_scoreboard.color("white")
        self.update_scores()

    def read_highscore(self):
        with open("Day_20\snake_game\data.txt", "r") as f:
            self.highscore = f.read()
            return int(self.highscore)

    def write_highscore(self):
        with open("Day_20\snake_game\data.txt", "w") as f:
            f.write(str(self.highscore))


    def update_scores(self):
        self.new_scoreboard.clear()
        self.new_scoreboard.write(f"Score is: {self.scores} Hight score is: {self.highscore} ", False, "center", ("Arial", 16, "normal"))


    def add_score(self):        
        self.scores += 1
        self.update_scores()
        self.new_scoreboard.ht()


    def reset_score(self):
        if self.scores > self.highscore:
            self.highscore = self.scores
            self.write_highscore()
        self.scores = 0
        self.update_scores()

    def game_over(self):        
        self.new_scoreboard.goto(0, 0)
        self.new_scoreboard.write(f"GAME OVER!", False, "center", ("Arial", 16, "normal"))



