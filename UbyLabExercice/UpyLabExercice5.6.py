"""
ncé
Voici le début d'une suite logique inventée par John Horton Conway (et donc appelée suite de Conway) :

    1
    11
    21
    1211
    111221
    312211
    ...
Chaque ligne à partir de la deuxième décrit la précédente...
La première ligne : 1,
on l'a décrit "Un 1" ce qui donne la deuxième : 11,
la troisième décrit la deuxième : "Deux 1" : 21
la quatrième décrit la troième : "Un 2 suivi de Un 1" : 1211
et ainsi de suite.

On vous demande d'écrire une fonction next_line(line) qui prend une liste d'entiers décrivant une ligne de cette suite et qui calcule et retourne la liste correspondant à la ligne suivante. Par exemple :

    next_line([1,2,1,1])

retourne la liste [1,1,1,2,2,1]

Par convention, next_line([]) retourne la liste [1]

"""




def next_line(line):
    L = len(line)
    print(L)
    newLine=[]
    occurence = 1

    if line == []:
        return [1]
    else:
        i=0
        for i in range(0, L):
            print("i:", i)

            if (i == L-1) or (line[i] != line[i+1]):
                if line[i] == line[i-1]:
                    newLine.append([occurence,line[i]])
                    occurence = 1
                elif line[i] != line[i-1]:
                    occurence = 1
                    newLine.append([occurence,line[i]])
                print('newLine :', newLine)

            elif line[i] == line[i+1]:
                    occurence += 1
                    print(occurence)

        i=i+1

    return sum (newLine,[])



print(next_line([1,2,1,1,1,1,2,2,2,1,3]))

