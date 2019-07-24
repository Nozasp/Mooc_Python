"""
Mise en pratique de la boucle for
"""

import turtle

"""
for i in range (4): # carré
    turtle.forward(100)
    turtle.left(90)
 """

#polygone a n cote

n = int(input("Nombre de côté : "))

if (n%2 == 0) :
    a = 360/n
else:
    a = ((n-1)*180)/n

for i in range(n) :
    turtle.forward(100)
    turtle.left(a)

turtle.done()