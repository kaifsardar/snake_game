from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0 # define by me
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}",align="center",font=("Arial",20,"normal"))
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=("Arial",24,"normal"))
    def increse_score(self):
        self.score+=1
        self.update_scoreboard()