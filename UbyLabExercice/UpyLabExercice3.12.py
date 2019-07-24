"""

Enoncé
Écrire un programme qui lit sur input une valeur naturelle n et qui affiche à l'écran un carré de n caractères X (majuscule) de côté, comme suit (pour n = 6):

XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX

Votre code ne doit pas tester si la valeur n est bien positive ou nulle.

Votre code à tester par upylab ne doit pas avoir de paramètre dans les input. Exemple : n = int(input()) plutôt que n = int(input("n = "))
"""

n = int(input())
for i in range (1, n+1):
    print("X"*n)


    """
    Variante de l'exercice "Carré de 'X'", afficher le triangle supérieur droit, comme suit (pour n = 6):

XXXXXX
 XXXXX
  XXXX
   XXX
    XX
     X"""


n = int(input())
print("X"*n)

for i in range (1, n):

    esp = (i-1)*" "

    print (esp,"X"*(n-1))
    n=n-1


for j in range(7):
    if j % 2 == 0:
        print(j+2)