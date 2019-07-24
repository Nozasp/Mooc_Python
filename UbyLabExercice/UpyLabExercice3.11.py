"""

TO FINISH !
Enoncé
On peut calculer approximativement le sinus de x
(voir définition du sinus) en effectuant la sommation des n premiers termes de la série (c'est-à-dire la somme infinie) :
sin(x)=x−x33!+x55!−x77!+...
où x est exprimé en radians.

On vous demande d'écrire un code qui lit une valeur flottante (float) x
en entrée et qui imprime une approximation de sin(x)

.

Votre code additionne les termes successifs dans la série jusqu'à ce que la valeur d'un terme devienne inférieure
 (en valeur absolue) à une constante ϵ
(prenez ϵ=10−6

). Affichez (imprimé) ensuite l'approximation ainsi obtenue.

Attention : Calculer explicitement la valeur des factorielles peut poser des soucis lorsque vous utilisez
les valeurs pour des calculs avec des float. Si c'est le cas, pensez à une autre façon de faire !
"""

from math import (sin)
import math

x = float(input())
E = 10**(-6) #constance limite

n = 0 #nombre en puissance ou en factoriel
facto =1 # valeur de la factorisation
i=1 # index
# initialisation des sin ?
terme = 1

while terme>= E:

    for i in range(1, n + 1): #on calcule la valeur de factorisation pour chaque index de n
        facto = facto * i
    print(facto)

    terme = abs((x ** n) / facto) #On calcule un terme. les terme vont s additionner ou se soustraire
    print(terme)
    print(i)
    if i%2 == 0:
        terme == - terme
    elif i%2 != 0:
        terme == terme

    terme = terme + terme
    sin(x) == terme

    n = n + 3
    i = i + 1
    print(sin(x))

print(abs(sin(x)))


"""
while abs(sin(x)) >= E:
    n = n + 2

    sin(x)==x - ((x**n)/(n!)
print(sin(x))"""