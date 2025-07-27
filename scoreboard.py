from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("highest_score.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.teleport(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} Highscore : {self.highscore} ", False, "center",
                   ("Arial", 12, "normal"))

    def reset(self):
        self.clear()
        if self.score >= self.highscore:
            self.highscore = self.score
            with open("highest_score.txt", "w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

