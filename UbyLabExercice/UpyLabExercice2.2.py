"""
Enoncé
Écrire un programme qui imprime le volume d'une sphère de rayon r
; le rayon étant lu sur input.
La formule de calcul du volume d'une sphère de rayon r
est donné par :

    volume = 4/3πr3

"""
from math import pi

r = float(input())

print((4/3)*pi*(r**3))



