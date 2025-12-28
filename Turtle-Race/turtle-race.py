import turtle
import random
from tkinter import messagebox

steps = [10,10,15,15,30,20]

is_race_on=False
screen = turtle.Screen()
screen.setup(height=400, width=600)
user_bet = screen.textinput("Make your bet","Enter the color of the turtle you want to bet:") 
colors = ["red", "blue", "green", "gold", "orange", "purple"]
y_positions = [-150,-100,-50,0,50,100]
all_turtles = []

line = turtle.Turtle()
line.speed(0)
line.penup()
line.goto(230,200)
line.pendown()
line.setheading(270)
line.forward(400)



for turtle_index in range(0,6):
    tim = turtle.Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(tim)


if user_bet:
    is_race_on=True

while is_race_on:

    for turtles in all_turtles:
        if turtles.xcor()>210:
            is_race_on=False
            winning_color = turtles.pencolor()
            if winning_color == user_bet.lower():
                print(f"You win, the {winning_color} turtle is the winner")
                messagebox.showinfo("Race Results", f"The {winning_color} Turtle Won! GG!")
            else:
                print(f"You lost, the {winning_color} turtle is the winner")
                messagebox.showinfo("Race Results", f"The {winning_color} Turtle Won! YOU LOST!")

        distance = random.randint(0,10)
        turtles.forward(distance)















# purple_turtle = turtle.Turtle()
# purple_turtle.color("purple")
# purple_turtle.goto(-250,150)
# purple_turtle.shape("turtle")

# blue_turtle = turtle.Turtle()
# blue_turtle.color("blue")
# blue_turtle.goto(-250,100)
# blue_turtle.shape("blue")

# yellow_turtle = turtle.Turtle()
# yellow_turtle.color("gold4")
# yellow_turtle.goto(-250,50)
# yellow_turtle.shape("turtle")

# green_turtle = turtle.Turtle()
# green_turtle.color("green")
# green_turtle.goto(-250,0)
# green_turtle.shape("turtle")

# cyan_turtle = turtle.Turtle()
# cyan_turtle.color("cyan")
# cyan_turtle.goto(-250,-50)
# cyan_turtle.shape("turtle")

# red_turtle = turtle.Turtle()
# red_turtle.color("red")
# red_turtle.goto(-250,-100)
# red_turtle.shape("turtle")

# black_turtle = turtle.Turtle()
# black_turtle.color("black")
# black_turtle.goto(-250,-150)
# black_turtle.shape("turtle")




turtle.done()

