"""
Ecrivez un programme qui teste si deux nombres entiers, a et b strictement supérieurs à 0, lus sur input sont tels que :

    a ne divise pas entièrement b sans reste et
    a n'est pas entièrement divisé par b sans reste.

Dans ce cas le programme imprime True ;

sinon il imprime False.
"""

a = abs (int (input()))
b = abs (int (input()))

if (a%b != 0) and (b%a != 0) :
    print("True")
else:
    print("False")

