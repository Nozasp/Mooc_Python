"""
Ecrivez une fonction my_pow qui prend comme paramètres un nombre entier m et un nombre flottant b et qui renvoie
une liste contenant les m premières puissances de b, c'est-à-dire une liste contenant les éléments allant de b0 à bm−1.

Si le type des paramètres n'est pas celui attendu, votre fonction renverra la valeur None
"""

def my_pow (m,b):
    if (type(m)== int) and (type(b) == float):
        ListePuissance = []
        i = 0
        for i in range(i, m):
            ListePuissance.append(b**i)
            i += 1
        return ListePuissance
    else:
        return None


print(my_pow(5,6.8))
