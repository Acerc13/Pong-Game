from turtle import Turtle , Screen


screen = Screen()

class Paddle(Turtle):
    def __init__(self, poss, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(poss)
        


#____________________________________________________________________________________
                                                                                    #
    def move_up(self):                                                              #         
        if self.ycor() <=  240 :
            y_cor = self.ycor() + 10                                                    #             
        x_cor = self.xcor()                                                         #           
        self.goto(x_cor,y_cor)                                                      #
                                                                                    #
                                                                                    #                    This function makes the paddle      
                                                                                    #                 Move up and down accoding to key press
                                                                                    #  
    def move_down(self):                                                            #          
        if self.ycor() >= -240:
            y_cor = self.ycor() - 10                                                    #
        x_cor = self.xcor()                                                         #
        self.goto(x_cor,y_cor)                                                      #
#___________________________________________________________________________________#
        


    

        

