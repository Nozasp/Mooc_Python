"""Écrire le morceau de code qui si, a (entier lu sur input) est supérieur à 0, teste si a vaut 1, auquel cas il imprime le texte :

"a vaut 1"

et qui, si a n’est pas supérieur à 0, imprime le texte :

"a est inférieur ou égal à 0"

Dans les autres cas, votre code n'imprime rien."""

a = int(input())

if a > 0 :
    if a == 1:
        print("a vaut 1")
elif a <= 0:
    print("a est inférieur ou égal à 0")