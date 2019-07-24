"""Enoncé
Écrivez une fonction fibo(n) qui reçoit un nombre entier : n
en paramètre, et qui, renvoie le n-ième nombre de Fibonacci Fi avec
F0
valant 0
F1
valant 1
Fi+1
valant Fi+Fi−1
Fn
valant None si n<0
Par ailleurs, écrivez le code principal: votre programme lira une donnée entière x de type int et
imprimera le résultat de l'exécution de fibo(i) pour i allant de 0 compris à x non compris avec chaque valeur sur une ligne séparée. """

def fibo(n): # indice du nombre de Fibonacci a calculer
    """calcule le nième nombre de Fibonacci, avec : n de type int et
    fibo(0) valant 0
    fibo(1) valant 1 et
    fibo(n+1) valant fibo(n-1) + fibo(n)
    si n < 0 : fibo(n) retourne None"""
    if n == 0 :
        res = 0
    elif n == 1 :
        res = 1
    elif n < 0 :
        res = None
    elif n > 1:
        prec = 0
        succ = 1
        for i in range (n-1):
            prec, succ = succ, prec + succ
        res = succ
    return res



x = int(input())


for x in range(0,x):
    print(fibo(x))
