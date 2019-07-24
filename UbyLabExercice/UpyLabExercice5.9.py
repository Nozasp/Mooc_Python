"""

Nous vous demandons d’écrire une fonction intersection(v, w) qui calcule l’intersection entre deux chaînes de caractères v et w.

On définit l’intersection de deux mots comme étant la plus grande partie commune à ces deux mots. Par exemple,
l’intersection de "programme" et "grammaire" est "gramm", et intersection("salut","rien") renvoie le string vide "",
puisqu'aucun caractère n'est commun.

Si plusieurs solutions sont possibles, prenez celle qui est d'indices les plus petits dans v (par exemple intersection
("bbaacc", "aabb") renvoie "bb".

"""

"""def intersection(v, w):
    res = []
    for i in v:
        if v(i) and v(i+1) in w:
            res.append(v(i))

    return res


print(intersection("grammaire","programme"))


  # if letter in w:
        #    res.append(letter)

"""

"""
def in_both(word1, word2):
 
 res=[]
 t = list(set(word1).intersection(set(word2)))
 for letter in word1:
   if letter in word2:
     res.append(letter)
 return t


print(in_both("grammaire","programme"))
"""


def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    return answer

def intersection(v, w):
    answer = []
    len1, len2 = len(v), len(w)
    for i in range(len1):
        match = []
        for j in range(len2):
            if (i + j < len1 and v[i + j] == w[j]):
                match += w[j]
            else:
                if (len(match) > len(answer)):
                    answer = match
                    if answer>1:
                        answer == min(answer)
                match = []
    return ''.join(answer)


print(intersection("applepieaavailablesa", "applepieasaa"))
print(intersection("aube", "beau"))
print(longestSubstringFinder("bapples", "cappleses"))
