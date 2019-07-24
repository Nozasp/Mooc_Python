
import turtle

from math import( cos , pi , sin)

long = abs(float(input("Longueur de l'arrête : ")))
angle = 120
for i in range(3):# à chaques itération, trace un losange
    turtle.begin_fill()
    if i == 1:
        turtle.color("blue")
    elif i == 2:
        turtle.color("dark blue")
    elif i == 3:
        turtle.color("dark")
    for j in range(4):
        turtle.forward(100)
        turtle.right(angle)
        print(angle)
        angle = 180 - angle

    turtle.right(120)
    turtle.end_fill()
turtle.done()