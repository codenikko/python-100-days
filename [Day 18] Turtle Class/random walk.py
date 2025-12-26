import turtle
import random
turtle.colormode(255)

tim = turtle.Turtle()
# tim.shape("turtle")
tim.speed(0)

# colors = [
#     "cornflower blue", "orchid", "tomato", "medium sea green", 
#     "gold", "deep sky blue", "slate blue", "hot pink", 
#     "firebrick", "dark violet", "turquoise", "sandy brown"
# ]



directions = [0, 90, 180, 270]

walk = [5,10,20,30,15,25,60]

tim.pen(pensize=10)


for _ in range(300):
    tim.color((random.randint(0, 255),random.randint(0, 255),random.randint(0,255)))
    tim.forward(random.choice(walk))
    tim.setheading(random.choice(directions))

    


screen = turtle.Screen()
screen.exitonclick()