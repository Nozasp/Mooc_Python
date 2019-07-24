import math
from math import sqrt

liste_premier = []

def premier(n):
    """ renvoie vrai si n est un nombre premier"""
    if n <= 1:
        return False
    for i in range(2, n+1):
        if n % i == 0:
           break
        else:
            return True



def premier(n):
    """ renvoie vrai si n est un nombre premier"""
    if n < 2:
        return False

    i = 2
    while i < n and n % i != 0:
        i += 1
    return i == n


# code principal
print("liste des nombres premiers jusqu'à 100")

for p in range(100):
    if premier(p):
        print(p)


x = int(input())

for p in range (2, x):
    if premier(p):
        print(p)
