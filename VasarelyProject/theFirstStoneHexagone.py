import turtle
# from math import cos,sin,pi

# longueur =100 angles : 120 ou 60

from math import (cos, pi, sin)

long = abs(float(input(" Renseignez la longueur de l'arrête :")))

alpha = float(pi/3)
beta = float(((2*pi)/3))
ceta = float(pi)
delta = float((4*pi)/3)
eta = float((5*pi)/3)

A = (float(long*cos(0)), float(long*sin(0)))
B = (float(long*cos(alpha)), float(long*sin(alpha)))
C = (float(long*cos(beta)), float(long*sin(beta)))
D = (float(long*cos(ceta)), float(long*sin(ceta)))
E = (float(long*cos(delta)), float(long*sin(delta)))
F = (float(long*cos(eta)), float(long*sin(eta)))



""" def pave(t, abscisse_centre, ordonnee_centre, longueur_arete, color1, color2, color3):
    turtle.shape(t)
    for i in range(3) :
     turtle.begin_fill(ordonnee_centre)
    if i == 1:
        turtle.color(color1)
    elif i == 2:
        turtle.color(color2)
    elif i == 3:
        turtle.color(color3)
    turtle.begin_fill(ordonnee_centre)
    for j in range(4) :
        turtle.forward(longueur_arete)
        turtle.goto(abscisse_centre,) 


pave('turtle',4,55,44,55,"blue","blue","red")"""

turtle.shape('turtle')
turtle.color('blue')
turtle.begin_fill()
turtle.forward(long)
turtle.goto(B)
turtle.goto(C)
turtle.goto(0, 0)
turtle.end_fill()
turtle.color("dark blue")
turtle.begin_fill()
turtle.goto(E)
turtle.goto(D)
turtle.goto(C)
turtle.end_fill()
turtle.up()


turtle.goto(E)
turtle.down()
turtle.color("black")
turtle.begin_fill()
turtle.goto(F)
turtle.goto(A)
turtle.goto(0, 0)
turtle.end_fill()

turtle.hideturtle()
turtle.done()
