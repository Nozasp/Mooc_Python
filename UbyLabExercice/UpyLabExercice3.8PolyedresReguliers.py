polyedre = input()
a = abs(float(input())) #arrete du polyedre

if polyedre == "T" : #tetraedre
    print(((2**0.5)/12)*(a**3))

elif polyedre == "C" : #Cube
    print(a**3)

elif polyedre == "O" : #Octaedre
    print(((2**0.5)/3)*(a**3))

elif polyedre == "D" : #Dodecaedre
    print(((15+7*(5**0.5))/4)*(a**3))

elif polyedre == "I" : # Icosaedre
    print(((5*(3+(5**0.5)))/12)*(a**3))

else: print("Polyèdre non connu")
