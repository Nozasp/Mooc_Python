"""Auteur : Kenza Garreau
But du document : Calcule des quantités d´ingrédients nécessaires pour la réalisation d´une mousse au chocolat dont le nombre de personne est donné en input
09.02.2019
Entrée : n, nombre de personne
Sortie : la quantité d´oeuf, de chocolat et le nombre de sachet de sucre vanille """

#Entrée du nombre de personne :
n = int(input("Nombre de gourmands :"))

#Calcule et imprime les résultats :
print("Nombre d´oeufs nécessaires : ", round((3*n)/4))
print("Quantité de chocolat (g) : ", round((100*n)/4))
print("Nombre de sachet de sucre vanille : ", max(round(n/4),1))



