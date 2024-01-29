from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("red")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=("Courier", 25, "bold"))
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=("Courier", 25, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def run(self):
        if self.l_score >= 25 or self.r_score >= 25 :
            return True
        if self.l_score + self.r_score <= 49 :
            return False
