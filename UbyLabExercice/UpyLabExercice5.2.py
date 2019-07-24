"""
Écrivez une fonction longueur(*points) qui prend en paramètres un nombre arbitraire de points de coordonnées (x,y)
et calcule la longueur du trait correspondant. Pour calculer la longueur, il faut effectuer la somme de la longueur des
segments qui composent le trait. Un segment de droite est composé de deux points consécutifs passés en paramètre.
Pour rappel, la distance entre deux points (x1,y1) et (x2,y2) se calcule comme suit:
dist=(x2−x1)2+(y2−y1)2−−−−−−−−−−−−−−−−−−√
Conseil: utilisez la fonction distances_points(p1, p2) définie avant.
"""
def distance_points (a,b) :
    from math import sqrt
    dist = sqrt(((b[0] - a[0])**2) + ((b[1] - a[1])**2))
    return dist



def longueur (*points):
    L = 0
    i=0
    while i < len(points):
        print(points)
        segment = distance_points(points)
        print(segment)
        segment = segment + L
        segment = L
        i =i+2
        print(i)



print(longueur(2,3,4,2,4,2))