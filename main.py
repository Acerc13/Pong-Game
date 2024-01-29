from turtle import Screen , Turtle
from paddle import Paddle
from ball import Ball
from dist import create_fild
from scorebord import Scoreboard
import time

ttt = Turtle()
scoreboard = Scoreboard()
screen = Screen()
screen.tracer(0)
create_fild()     
paddle_0 = Paddle((350,0))
paddle_1 = Paddle((-350,0))
ball = Ball()

is_on = True



#----------------------------------------------------------------#
                                                                 #
screen.bgcolor('black')                                          #          Setting the screen color
screen.setup(width=800, height=600)                              #          Setting the screen csize
screen.title("PonG")                                             #
screen.listen()                                                  #
                                                                 #
                                                                 #  
#----------------------------------------------------------------#


#_______________________________________________________________#
                                                                #
screen.onkey(paddle_0.move_up,key= "Up")                        #
screen.onkey(paddle_0.move_down,key= "Down")                    #        Giving key inputs
screen.onkey(paddle_1.move_up,key= "w")                         #
screen.onkey(paddle_1.move_down,key= "s")                       #
#_______________________________________________________________#




                                    # Creating a while loop to keep it going
#####################################################################################################################################################################################################
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#####################################################################################################################################################################################################
while is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()
    print(ball.xcor())



    if ball.ycor() > 285 or ball.ycor() < -285 : # Checking if the ball is touching or about to touch
        ball.bounce_from_wall()                       #the walls up and down and bounce it 




    if ball.distance(paddle_0) < 50 and ball.xcor() > 329 or ball.distance(paddle_1) < 50  and ball.xcor() < -329 :         # Checking if the ball is touching or about to touch
        ball.bounce_from_paddle()                                                                                                # he walls up and down and bounce it 
        print("crash")


    if ball.xcor() > 370 :
        ball.reset_pos()
        scoreboard.l_point()
    
    if ball.xcor() < -370 :
        ball.reset_pos()
        scoreboard.r_point()
    
    if scoreboard.run():
        ttt.hideturtle()
        ttt.penup()
        ttt.color("Green")
        ttt.write("Game Over" , align="center", font=("Arial",35,"bold"))

        break

    




                                                  # End of the Loop
######################################################################################################################################################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
######################################################################################################################################################################################################
    



screen.exitonclick()