"""
Écrire un programme qui lit ce que mise le joueur parmi :

    0, 1, ..., 12
    13 pour "Pair"
    14 pour "Impair"
    15 pour "Rouge"
    16 pour "Noir"

et qui, après avoir actionné la roulette et reçu un nombre x entre 0 et 12, imprime le retour correspondant, soit:

    12 si le numéro exact est trouvé,
    2 si Pair/Impair ou Rouge/Noir est gagné,
    0 si le pari est perdu.

Par exemple si la pari est 14 ("Impair") et que 7 est sorti par la roulette, le résultat est : 2

Comme malheureusement nous n'avons pas de roulette à notre disposition, pour tester votre code, celui-ci débutera par les deux premières lignes suivantes :

"""

a = int(input()) # reçoit le pari du joueur entre 0 et 16
x = int(input()) # reçoit la valeur du tirage entre 0 et 12

if a == x :
    print("12")

elif ((x == 2 or x==4 or x==6 or x==8 or x==10 or x==11) and (a == 16)):
    print("2")

elif (x == 1 or x==3 or x==5 or x==7 or x==9 or x==12) and a == 15:
    print("2")


elif (a == 13 ) and (x%2 == 0):
    print("2")

elif(a ==14) and (x%2 != 0) :
    print("2")

else:
    print("0")