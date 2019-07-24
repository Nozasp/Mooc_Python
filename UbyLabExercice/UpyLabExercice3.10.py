"""
 Écrivez un mini jeu : le programme génère de manière (pseudo-) aléatoire un nombre naturel (nombre secret) dans l'intervalle entre 0 et 100.
Ensuite, le joueur doit deviner ce nombre en utilisant le moins d'essais possible.
A chaque tour le joueur peut faire un essai et le programme doit donner une parmi les réponses suivantes:

    "Trop grand" : Si le nombre secret est plus petit et qu'on n'est pas au maximum d'essais
    "Trop petit" : Si le nombre secret est plus grand et qu'on n'est pas au maximum d'essais
    "Gagné en n essais !" : Si le nombre secret est trouvé
    "Perdu ! Le secret était", nombre : Si vous avez fait 6 essais sans trouver le nombre secret

Le joueur a maximum 6 essais ; s'il ne devine pas le secret après 6 essais, le programme s'arrête après avoir écrit "Perdu ! Le secret était", nombre"
Exemple d’exécution gagnante (après la génération du nombre à deviner):

    50
    Trop grand
    8
    Trop petit
    20
    Trop petit
    27
    Gagné en 4 essais !

Exemple d’exécution perdante (après la génération du nombre à deviner):

    50
    Trop grand
    24
    Trop petit
    "37
    Trop petit
    43
    Trop grand
    40
    Trop petit
    41
    Perdu ! Le secret était 42


"""

"""
import random
secret = random.randint(0,100)
n=0

for i in range (6) :
    choix_utilisateur = int(input())
    n = n+1
    if secret < choix_utilisateur and n !=6 : print("Trop grand")
    elif secret > choix_utilisateur and n !=6 : print("Trop petit")
    elif secret == choix_utilisateur: print("Gagné en ",n," essais !")

if n == 6 and secret != choix_utilisateur : print("Perdu ! Le secret était ",secret)
"""


import random
random.seed(22)
secret = random.randint(0,100)
nbEssaiMax=6
n = 0

for i in range (nbEssaiMax) :
    choix_utilisateur = int(input())
    n = n+1
    if secret == choix_utilisateur: break
    elif n == 6 : print("Perdu ! Le secret était ", secret)
    elif secret < choix_utilisateur: print("Trop grand")
    elif secret > choix_utilisateur: print("Trop petit")

if secret == choix_utilisateur : print("Gagné en", n, "essais !")

