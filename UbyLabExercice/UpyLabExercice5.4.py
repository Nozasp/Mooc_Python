"""
 Ecrire une fonction trans(text, replaceA, replaceB), qui reçoit trois paramètres:
text : une chaîne de caractères
replaceA : un couple (oldA, newA) où oldA est un caractère et newA un texte
replaceB : un couple (oldB, newB) où oldB est un caractère et newB un texte
et qui renvoie le résultat de la transformation suivante : chaque occurrence du symbole "oldA" dans la chaîne text est
remplacée par la chaîne "newA", et simultanément chaque occurrence du symbole "oldB" est remplacée par la chaîne "newB".

Pour simplifier, vous pouvez supposer que "oldA" est différent de "oldB"

Exemple:

#>>> print(trans('ABBAB', ('A','AB'), ('B','BA')))
#>>> 'ABBABA ABBA'


"""


"""
def trans (text, replaceA, replaceB):
    text = input()
    oldA = eval(int(input()))
    newA = eval(input())
    oldB = eval(int(input()))
    newB = eval(input())
    replaceA = [oldA], newA
    replaceB = [oldB], newB

    oldA, newA = newA, oldA
    oldB, newB = newB, oldB

"""
#  newA = eval(input())

def trans (text, replaceA, replaceB):
    oldA = replaceA[0]
    oldB = replaceB[0]
    newA = replaceA[1]
    newB = replaceB[1]
    L = len(text)
    LoA = len(oldA)
    LoB = len(oldB)
    LnA = len(newA)
    LnB = len(newB)
    text2=[]

    if type(text) == str:
        if (LoA ==1 and LoB == 1 ) and (LnA >=1 and LnB >= 1):
            print(oldA, oldB, newA, newB, L, text[0], text[1])
            i = 0
            for i in range (0, L) :
                print(i)
                if text[i] == oldA:
                    #text2 = text2 + newA + text[i + 1:]
                    #text[i] == newA
                    text2.append(newA)
                    print("newA", text2)
                elif text[i] == oldB:
                    #text2 = text2 + newB + text[i+1:]
                    text2.append(newB)
                    #new_text.append(newB)
                    print("newB",text2)
                else: text2.append(text[i])
                i = i+1

            return ''.join(text2)






print(trans("allo",("a","mar"),("l","kus")))


