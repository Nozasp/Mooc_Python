"""
Enoncé
Écrire un programme, qui lit une longueur long de type float, strictement positive et qui affiche les valeurs x y des
coordonnées (x, y) des sommets de l'hexagone de centre (0,0) et de rayon long, dans l'ordre donné par le point à 0°
 ensuite 60°, 120° jusqu'au 6ème point).
Chaque couple de coordonnées sera affiché sur une ligne différente.

"""

from math import(cos,pi,sin)

long = abs(float(input()))

alpha= float(pi/3)
beta= float(((2*pi)/3))
ceta= float(pi)
delta= float((4*pi)/3)
eta= float((5*pi)/3)

print(float(long*cos(0)), float(long*sin(0)))
print(float(long*cos(alpha)), float(long*sin(alpha)))
print(float(long*cos(beta)), float(long*sin(beta)))
print(float(long*cos(ceta)), float(long*sin(ceta)))
print(float(long*cos(delta)), float(long*sin(delta)))
print(float(long*cos(eta)), float(long*sin(eta)))




