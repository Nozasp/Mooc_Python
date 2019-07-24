"""
Petit jeu de devinette version 1 :
tirage aléatoire d´un entier entre 0 et 5 et demande à
l´utilisateur de trouver le chiffre.
Auteur : Kenza Garreau
Date : 17 février 2019
"""

import random
secret = random.randint(0,5)

choix_utilisateur = int(input("Devinez la valeur choisi par l´ordinateur. Veuillez saisi un chiffre entre 0 et 5 : \n "))


if secret == choix_utilisateur:
    print("C´est gagné ! =)")
else:
    print ("C´est perdu ! la valeur choisi était : ", secret)


