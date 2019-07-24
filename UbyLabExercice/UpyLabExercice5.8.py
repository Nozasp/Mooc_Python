"""
Veuillez écrire une fonction anagrammes(v, w) qui renvoie la valeur booléene True si les mots v et w sont des anagrammes,
c’est-à-dire des mots qui comprennent les mêmes lettres, en même quantité, mais pas nécessairement dans le même ordre.
Par exemple, 'marion' et 'romina' sont des anagrammes.

La fonctio renvoie la valeur booléenne False sinon

Notes :
Votre code ne doit pas tester si les mots existent bien dans un quelconque dictionnaire
On suppose que tout mot est anagramme avec lui même
(par exemple: anagrammes('jour', 'jour') renvoie True)
"""

def anagrammes(v, w):
 """Renvoie la liste des lettres communes aux 2 mots."""

 res=[]
 for letter in v:
     if letter in w :
         res.append(letter)
         if len(v) == len(w) == len(res):
             return True
 else : return False



print(anagrammes("marion","rominam"))



