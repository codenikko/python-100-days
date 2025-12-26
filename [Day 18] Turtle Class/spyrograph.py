import turtle
import random
turtle.colormode(255)

t = turtle.Turtle()
t.speed(0)

for i in range(72):
    t.color((random.randint(0, 255),random.randint(0, 255),random.randint(0,255)))
    t.circle(80)
    t.left(5)

turtle.done()
