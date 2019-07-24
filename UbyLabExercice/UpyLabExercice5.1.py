"""
Écrivez une fonction distance_points() qui, étant donnés deux points (x1,y1) et (x2,y2) reçus en paramètres sous forme de tuples,
 calcule et renvoie la distance euclidienne entre ces deux points. Pour rappel,
 la distance entre deux points (x1,y1) et (x2,y2) se calcule comme suit:
dist=(x2−x1)2+(y2−y1)2−−−−−−−−−−−−−−−−−−√
où a−−√ est la racine carrée de a et correspond à a1/2 (a
exposant un demi).
Entrez votre solution :
"""

def distance_points3 (x1,y1,x2,y2) :
    a = (x1, y1)
    b = (x2, y2)
    from math import sqrt
    dist = sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    return dist


def distance_points2 (*parametre) :
    from math import sqrt
    dist = sqrt(((parametre[2] - parametre[0])**2) + ((parametre[3] - parametre[1])**2))
    return dist


def distance_points (a,b) :
    from math import sqrt
    dist = sqrt(((b[0] - a[0])**2) + ((b[1] - a[1])**2))
    return dist



print(distance_points ((-2.0, 2.5),(-1.5, 4.0)))