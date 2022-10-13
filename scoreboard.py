from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(0, 270)
        self.count_score()


    def count_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", align="center", font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
            self.score = 0
            self.count_score()

    def increase_score(self):
        self.score += 1
        self.count_score()
    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align="center", font=("Arial", 15, "normal"))

