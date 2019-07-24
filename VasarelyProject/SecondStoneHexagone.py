
import turtle

from math import(cos,pi,sin)

color1 ="blue"
color2 = "dark blue"
color3 = "dark"


def pave(t, abscisse_centre, ordonnee_centre, longueur_arete, color1, color2, color3):
    abscisse_centre, ordonnee_centre = (0, 0)
    longueur_arete = abs(float(input()))
    angle = 120
    for i in range(3) : # à chaque itération, trace un losange
     turtle.begin_fill()
    if i == 1:
        turtle.color(color1)
    elif i == 2:
        turtle.color(color2)
    elif i == 3:
        turtle.color(color3)
    for j in range(4) :
        turtle.forward(longueur_arete)
        turtle.right(angle)
        print(angle)
        angle = 180 - angle

    turtle.right(120)
    turtle.end_fill()
turtle.done()