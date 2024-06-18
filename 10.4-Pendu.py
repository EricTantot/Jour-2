motMystere = input("Entrer un mot mystère de 6 à 10 lettres: ")
lettres = []

place = []
lenght = len(motMystere)
x = 0

while x < lenght :
    x = x + 1
    place.append(x)

for lettre in motMystere:
    lettres.append(lettre)

final = list(zip(lettres,place))
n = len(lettres)
found = 0
total = 0 
win = 0
trouvé = []

def trouver_numéro(a, final):
    for i in final:
        if i[0] == a:
            return i[1]

if n < 6:
    print("Veuillez entrer un mot de 6 à 10 lettres.")
elif n > 10:
    print("Veuillez entrer un mot de 6 à 10 lettres.") 
else:
    print(f"Vous avez {n} essais pour trouver le mot mystère → {'_'*n}")
    while total < n :
        test = input("Entrer une lettre ou un mot: ")
        if len(test) > 1:
            if test == motMystere:
                win = win + 1
                break
            else: 
                total = total + 1
                print(f"Mauvais mot! Il vous reste {n-total} essais.")
        else:
            if test in trouvé:
                print(f"Vous avez déjà proposé cette lettre: {test}")
            else: 
                if test in lettres:
                    trouvé.append(test)
                    found = found + 1
                    if found == n :
                        win = win + 1
                        break
                    else:
                        a = trouver_numéro(test, final)
                        print(f"Vous avez trouvé une lettre: {test}, elle est à la {a}e place, il vous en reste {n-found} à trouver!")
                else: 
                    total = total + 1
                    trouvé.append(test)
                    print(f"Mauvaise lettre! Il vous reste {n-total} essais.")

    if win == 0:
        print(f"Perdu! Le mot était {motMystere}!")
    else:
        print(f"Vous avez trouvé le mot {motMystere}. Bien joué!")
