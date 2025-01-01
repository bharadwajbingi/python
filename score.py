from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt') as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.pencolor('white')
        self.goto(-150, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score : {self.high_score} ", font=("Arial", 18, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt',mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_score(self):
        self.score += 1
        self.update_scoreboard()
