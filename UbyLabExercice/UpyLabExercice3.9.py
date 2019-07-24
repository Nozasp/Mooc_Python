"""

Enoncé
Écrire un programme qui calcule la taille moyenne (en nombre de personnes) des Petites et Moyennes Entreprises de la
région, les tailles étant données en input; la fin des données étant signalée par la "valeur sentinelle" −1
qui ne fait pas partie des éléments à comptabiliser mais indique que l'ensemble des valeurs a été donné.

On suppose aussi que la suite des tailles contient toujours au moins un élément avant la valeur sentinelle -1
et que toutes ces valeurs sont positives ou nulles. Après l'entrée de la valeur sentinelle, le programme affiche
sur la ligne suivante la valeur de la moyenne arithmétique.

Exemple d’exécution : avec les valeurs lues suivantes :

    11
    8
    14
    5
    -1

le résultat que doit donner votre code est :

    9.5

"""

taille = 0
n = 0
add = 0

while add != (-1) :
    add = int (input())
    taille = taille + add
    n = n+1


print((taille+1)/(n-1))


