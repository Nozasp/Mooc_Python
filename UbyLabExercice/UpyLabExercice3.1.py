"""
Écrire un programme qui lit 3 nombres entiers, et qui,
si au moins deux d’entre eux ont la même valeur,
imprime cette valeur
(le programme n’imprime rien dans le cas contraire).
"""

a = int(input())
b = int(input())
c = int(input())

if (a==b) or (a==c) or (b==c):
    if (a==b) or (a==c):
        print(a)
    else: print(b)

