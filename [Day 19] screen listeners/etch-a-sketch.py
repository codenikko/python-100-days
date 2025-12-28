import turtle

tim = turtle.Turtle()
screen = turtle.Screen()
tim.speed("fastest")

screen.listen()


def move_up():
    tim.forward(10)
        

def move_down():
   tim.back(10)

def move_left():
    tim.setheading(tim.heading() + 10)
    

def move_right():
    tim.setheading(tim.heading() - 10)
    


screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(tim.penup, "'")
screen.onkey(tim.pendown, "/")
screen.onkey(tim.reset, "c")

turtle.done()