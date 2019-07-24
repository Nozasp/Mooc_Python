"""
Soit l'équation du second degré
ax2+bx+c=0
paramétrée par a, b et c. Écrivez une fonction rac_eq_2nd_deg prenant 3 paramètres qui calcule et renvoie la ou les
solutions s'il y en a. Le résultat sera un tuple avec les racines :
Si il n'y a pas de solution réelle, renvoyez un tuple vide :

    return tuple()

Si il y a une seule racine r1, terminez votre code en renvoyant le résultat avec

    return (r1,)

Dans le cas où il y a deux solutions réelles r1 et r2, la plus petite devra être dans la première composante du tuple
renvoyé (composante d'indice 0). Vous pouvez utiliser

    return (min(r1,r2), max(r1,r2)).


"""
import math

a = int (input())
b = int (input())
c = int (input())

def rac_eq_2nd_deg (a, b ,c):
    discr_trinome = (b**2) - (4*a*c)
    print(discr_trinome)

    if discr_trinome < 0 :
        return tuple()

    if discr_trinome == 0:
        return ((-b)/(2*a),)

    if discr_trinome > 0:
        r1 = ((-b) - math.sqrt(discr_trinome))/(2*a)
        r2 = ((-b) + math.sqrt(discr_trinome))/(2*a)
        return (min(r1, r2), max((r1, r2)))


print(rac_eq_2nd_deg(a,b,c))