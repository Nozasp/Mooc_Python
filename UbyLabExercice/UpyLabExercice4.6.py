"""
Dans le module random, la fonction randint(a, b) renvoie un nombre entier aléatoire compris entre a et b (inclus).
Écrivez une fonction alea_dice qui génère 3 nombres aléatoires représentant 3 dés à jouer
(à six faces avec les valeurs 1 à 6) et qui renvoie la valeur booléenne True si les dés forment un 421,
et la valeur booléenne False sinon.

Prenez garde que toute combinaison des trois dés avec un 4, un 2 et un 1 forme 421 quelque soit l'ordre de la combinaison
(par exemple 2, 1 et 4 forme bien un 421.
"""

import random


def alea_dice(s):
    random.seed(s)
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)
    print(a)
    print(b)
    print(c)

    if (a,b,c) == ((4,2,1) or (4,1,2) or (2,4,1)):
        return True
    elif (a,b,c) == ((1,2,4)):
        return True
    elif (a,b,c) == ((2,1,4)):
        return True
    elif (a, b, c) == ((1,4,2)):
        return True
    else:
        return False


print(alea_dice(98088))

98088