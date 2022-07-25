from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
with open("score.txt") as saved_score:
    high_score = saved_score.read()
    highscore = int(high_score)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()




    def reset(self):
        with open("score.txt") as saved_score:
            high_score= saved_score.read()
            highscore = int(high_score)
            print(highscore)

        if  self.score> highscore:
            with open("score.txt", mode = "w") as saved_score:
                saved_score.write(f"{self.score}")
        self.score =0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("score.txt") as saved_score:
            high_score = saved_score.read()
            highscore = int(high_score)
        self.write(f"Score: {self.score}, High_Score = {highscore}", align=ALIGNMENT, font=FONT)


   # def game_over(self):
    #    self.goto(0, 0)
   #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

        self.update_scoreboard()
