"""
Il est demandé d'additionner des valeurs naturelles lues sur input et d'imprimer le résultat.
La première donnée lue ne fait pas partie des valeurs à sommer. Elle détermine si la liste contient un nombre déterminé à l'avance de valeurs à lire ou non.

    si cette première donnée vaut un nombre positif ou nul, ce nombre donne le nombre de valeurs à lire et à sommer
    si la donnée est négative, cela signifie que la liste des données à lire sera terminée par un caractère "F" signifiant que la liste est terminée

Exemple 1: les données lues suivantes:

    4
    1
    3
    5
    7

indiquent qu'il y a 4 données à sommer : 1 + 3 + 5 + 7.
Le résultat à imprimer vaudra donc 16

Exemple 2: les données lues suivantes:

    -1
    1
    3
    5
    7
    21
    F

indiquent qu'il faut sommer : 1 + 3 + 5 + 7 + 21. Le résultat à imprimer vaudra donc 37.

Exemple 3: La donnée

    0

indique qu'il faut sommer 0 nombre. Le résultat à imprimer vaudra donc 0.

Conseils:

    Dans la cas où la liste est terminée par le caractère 'F', vous pouvez d'une part faire l'input (ex : data = input()),
    ensuite tester si data == 'F' et sinon additionner la valeur int(data) à ce qui a déjà été sommé;
    Utilisez un for dans le cas où le nombre de valeurs à sommer est connu, un while dans le cas contraire.

Consignes:

    Ne mettez pas de paramètre texte dans les input: data = input() et pas data = input("Donnée suivante :")) par exemple;
    Le résultat doit juste faire l'objet d'un print(res) sans texte supplémentaire (pas de print("résultat =", res) par exemple).


"""


premiere_data = int(input())
datas = 0

if premiere_data>=0 :
    for i in range (0, premiere_data):
        datas = datas + int(input())
        i += 1
    print(datas)


if premiere_data< 0:
    data = 0
    somme = 0
    while data != 'F':
        data = input()
        if data == 'F':
            break
        elif data != 'F':
            data1 = int(data)
            data1 = data1 + somme
            somme = data1
    print(data1)




