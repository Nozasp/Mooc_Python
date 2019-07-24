"""Calcule du Nombre Catalan d´indice n"""

def facto (nb):
    for i in range(1, nb): #on calcule la valeur de factorisation pour chaque index de n
        nb = nb * i
    return nb


def catalan (n) :
    if n == 0:
        return 1
    else:
        return (facto(2*n))//((facto(n+1))*facto(n))


indice = abs(int(input()))

print(catalan(indice))