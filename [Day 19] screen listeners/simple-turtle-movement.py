import turtle

tim = turtle.Turtle()
screen = turtle.Screen()
tim.speed("fastest")

screen.listen()


def move_up():
    current_heading = tim.heading()
    if current_heading == 90.0:
        tim.forward(10)
    else:
        tim.setheading(90)
        

def move_down():
    current_heading = tim.heading()
    if current_heading == 270.0:
        tim.forward(10)
    else:
        tim.setheading(270)

def move_left():
    current_heading = tim.heading()
    if current_heading == 180.0:
        tim.forward(10)
    else:
        tim.setheading(180)

def move_right():
    current_heading = tim.heading()
    if current_heading == 0.0:
        tim.forward(10)
    else:
        tim.setheading(0)


screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(tim.penup, "'")
screen.onkey(tim.pendown, "/")

turtle.done()