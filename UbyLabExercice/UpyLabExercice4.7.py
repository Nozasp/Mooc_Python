"""
é
Considérons les billets et pièces de valeurs suivantes : 20 euros, 10 euros, 5 euros, 2 euros, 1 euros.
Écrivez une fonction rendre_monnaie qui prend en paramètres un entier prix et cinq valeurs entières x20, x10, x5, x2, x1
représentant le nombre de billets et de pièces de chaque sorte que donne un client pour payer l’objet dont le prix est mentionné.
La fonction doit renvoyer cinq valeurs représentant la somme qu’il faut rendre au client, décomposée en billets et pièces
(dans le même ordre que précédemment). La décomposition doit être faite en rendant le plus possible de billets et pièces de grosses valeurs
(éventuellement avec d'autres billets que ceux apportés par le client; on suppose qu'il y a toujours assez de billets chez le vendeur).

Pour renvoyer les cinq valeurs, vous utilisez l'instruction:

    return res20, res10, res5, res2, res1

où les cinq variables res20 à res1 contiennent les cinq valeurs à renvoyer (res20 contient le nombre de billets de 20 à
remettre, ..., res1 le nombre de pièces de 1 à remettre).

S'il manque de l'argent, la fonction renverra cinq valeurs None.
"""

#monnaie = (20,10,5,2,1)

def rendre_monnaie (prix,x20, x10, x5, x2, x1) :
    don = (x20*20) + (x10*10) + (5*x5) + (2*x2) + (1*x1)
    monnaie = don - prix
    print(monnaie)
    res20 = 0
    res10 = 0
    res5 = 0
    res2 = 0
    res1 = 0

    if don >= prix :
        while monnaie >= 20:
            monnaie = monnaie-20
            res20 = res20 + 1

        while monnaie >= 10:
            monnaie = monnaie-10
            res10 = res10 + 1


        while monnaie >= 5:
            monnaie = monnaie-5
            res5 = res5 + 1

        while monnaie >= 2:
            monnaie = monnaie-2
            res2 = res2 + 1

        while monnaie >= 1:
            monnaie = monnaie-1
            res1 = res1 + 1

        return res20, res10, res5, res2, res1

    else :
        return None, None, None, None, None

print(rendre_monnaie(100, 4, 3, 4, 5, 1))