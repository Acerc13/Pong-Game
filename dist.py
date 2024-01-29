from turtle import Turtle


tr = Turtle()

def create_fild():
    tr.penup()
    tr.color("white")
    tr.goto(400,300)
    tr.pendown()
    tr.pensize(5)
    tr.setheading(180)
    tr.forward(800)
    tr.setheading(270)
    tr.forward(600)
    tr.setheading(0)
    tr.forward(800)
    tr.setheading(90)
    tr.forward(600)
    tr.hideturtle()
