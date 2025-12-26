from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

colors = [
    "cornflower blue", "orchid", "tomato", "medium sea green", 
    "gold", "deep sky blue", "slate blue", "hot pink", 
    "firebrick", "dark violet", "turquoise", "sandy brown"
]

for n in range (3,11):
    tim.color(random.choice(colors))
    angle = ((n-2)*180)/n
    for i in range(n):
        tim.forward(50)
        tim.right(180-angle)


screen = Screen()
screen.exitonclick()