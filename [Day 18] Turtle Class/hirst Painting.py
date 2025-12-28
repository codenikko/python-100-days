import turtle
turtle.colormode(255)

import random


tim = turtle.Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101



for i in range(1,number_of_dots):
    tim.dot(15, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    tim.forward(50)

    if i%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
turtle.done()
