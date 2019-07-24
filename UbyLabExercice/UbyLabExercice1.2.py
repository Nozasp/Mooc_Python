"""
Enoncé
La règle de trois est une méthode pour trouver le quatrième terme parmi quatre termes ayant un même rapport de proportion ab=cd
, lorsque trois de ces termes sont connus.

    Par exemple si chacun mange autant de chocolat et que pour 4 personnes il en faut 100 grammes, pour 7 personnes il en faudra donc 74.100

grammes = 175

    grammes.

    Dans cet exemple a=4

, b=100, c=7 et d=175 : la règle est que l'on veut que chacun ai la même quantité de chocolat; donc il faut respecter le rapport 4100=7175

Elle utilise le fait que le produit des premier et quatrième termes est égal au produit du second et du troisième: a.d=b.c et donc d=c.ba
Écrire un programme qui lit les valeurs de type float pour a
, b et c et qui affiche la valeur de d
correspondant à la règle de trois.
Votre code à tester par UpyLaB ne doit pas avoir de paramètre dans les input. Exemple: a = float(input()) plutôt que a = float(input("a = "))
De même, votre code à tester par UpyLaB ne doit imprimer que le résultat numérique de d
, pas de texte supplémentaire. Exemple: print(d) plutôt que print("Résultat : ", d))
Le but de cet exercice est de vous familiariser avec la lecture (input()) de données et l'impression (print()) de résultats.

"""

a=float(input())
b=float(input())
c=float(input())

d = (b*c)/a

print(d)