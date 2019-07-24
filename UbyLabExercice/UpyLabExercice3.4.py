"""
 Ecrivez un programme qui teste la parité d'un nombre entier lu sur input
 et imprime True si le nombre est pair, False dans le cas contraire.
"""

nombreSelectionne = int(input())

if nombreSelectionne % 2 == 0 :
    print("True")
else:
    print("False")