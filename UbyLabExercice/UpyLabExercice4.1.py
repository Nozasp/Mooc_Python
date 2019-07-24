"""
Enoncé
Écrire une fonction deux_egaux(a, b, c) qui reçoit 3 nombres entiers ou float en paramètre, et qui, renvoie la valeur
booléenne True si au moins deux d’entre eux ont la même valeur et la valeur booléenne False sinon.

Par ailleurs, votre programme lira 3 données de type int x, y et z et imprimera le résultat de l'exécution de deux_egaux(x, y, z)
Votre code à tester par UpyLaB

    ne doit pas avoir de paramètre dans les input.
        Exemple: x = int(input()) plutôt que x = int(input("x = "))
    ne doit pas dans les print imprimer autre chose que le résultat (dans ce cas-ci True ou False)
        Exemple: print(deux_egaux(x, y, z)) plutôt que print("Résultat : ", deux_egaux(x, y, z))
    dans la fonction deux_egaux ne doit pas tester le type des paramètres reçus


"""

def deux_egaux(a,b,c):
    """Renvoie vrai si et seulement si deux chiffres sont similaires."""
    return a==b or b==c or a==c

x=int(input())
y=int(input())
z=int(input())

print(deux_egaux(x,y,z))