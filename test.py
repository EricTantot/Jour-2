motMystere = input("Entrer un mot mystère de 6 à 10 lettres: ")

place = []
lenght = len(motMystere)
x = 0

while x < lenght :
    x = x + 1
    place.append(x)

lettres = []
for lettre in motMystere:
    lettres.append(lettre)

final = list(zip(lettres,place))

def trouver_numéro(a, final):
    for i in final:
        if i[0] == a:
            return i[1]



