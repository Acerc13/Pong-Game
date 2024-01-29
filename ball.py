from turtle import Turtle , Screen
import random


class Ball(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        
        self.color("lightblue")
        self.shape("circle")
        self.penup()
        self.xmove = 3
        self.ymove = 3
        self.move_speed = 0.1




    def move(self):
        
        x_cor = self.xcor() + self.xmove
        y_cor = self.ycor() + self.ymove

        self.goto(x= x_cor,y=y_cor)

    def bounce_from_wall(self):
        self.xmove += 1
        self.ymove *= -1
        self.move_speed *= 1
    
    def bounce_from_paddle(self):
        self.ymove += 1
        self.xmove *= -1
        self.move_speed *= 0.75


    def reset_pos(self):
        self.goto(0,0)
        x = random.randint(1,2)
        self.xmove *= -1
        
        if self.xmove == 0 or self.ymove == 0 :
            self.xmove += 2
            self.ymove += 1
        elif -5 <= self.xmove and 5 >= self.xmove :
            if x == 1:
                self.ymove *= -1 
                self.xmove += x
            else:
                self.ymove *= 1
                self.xmove -= x
            
        else : self.xmove = 3
    