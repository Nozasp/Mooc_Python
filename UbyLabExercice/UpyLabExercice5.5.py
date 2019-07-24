"""

Écrivez une fonction duree qui prend deux paramètres debut et fin. Ces derniers sont des couples
(tuples de 2 composantes) dont la première composante représente une heure et la seconde composante représente les minutes.
 Cette fonction doit calculer le nombre d'heures et de minutes qu'il faut pour passer de debut à fin.
Exemple : un appel à duree ((14, 39), (18, 45)) renvoie (4, 6) pour 4 heures et 6 minutes.
Notez qu'un appel à duree ((6, 0), (5, 15)) renvoie (23, 15) pour 23 heures et 15 minutes, et non (0, 45) !

"""

def duree (debut, fin):
    heureD = debut[0]
    heureF = fin[0]
    minutesD= debut[1]
    minutesF= fin[1]
    if heureF>heureD:
        if minutesD>minutesF:
            heure_appel = heureF - heureD -1
        else :
            heure_appel = heureF - heureD

    elif heureF<heureD:
        if minutesD > minutesF:
            heure_appel = (24 - heureD) + heureF -1
        else:
            heure_appel = (24 - heureD) + heureF

    if minutesF>minutesD:
        minute_appel = minutesF - minutesD

    elif minutesD>minutesF:
        minute_appel = (60 - minutesD) + minutesF

    return (heure_appel, minute_appel)

print(duree((22, 21), (3, 17)))

