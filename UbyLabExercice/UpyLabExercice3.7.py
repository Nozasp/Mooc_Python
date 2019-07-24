"""
Écrire un programme qui imprime la moyenne géométrique a.b−−−√ (la racine carrée du produit de a par b)
de deux nombres positifs de type float lus sur input.
 Si au moins un des deux nombres est négatif, imprime "Erreur".
"""

a = float(input())
b = float(input())

x = a*b

if (a >=0 and b >= 0) :
    print(x**0.5)

else:
    print("Erreur")