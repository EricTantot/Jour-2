motMystere = input("Entrer un mot mystère de 6 à 10 lettres: ")
mots = []

for lettre in motMystere:
    mots.append(lettre)

n = len(mots)
x = len(mots)
bon = 0

if n < 6:
    print("Veuillez entrer un mot de 6 à 10 lettres.")
elif n > 10:
    print("Veuillez entrer un mot de 6 à 10 lettres.") 
else:
    print(f"Vous avez {n} essais pour deviner le mot mystère: {'_'*n}")
    while x == 0:
        essai = input("Entrer une lettre: ")
        if essai in mots :
            print(f"Une lettre trouvé: {essai}")
            bon = bon + 1
            if bon == n:
                print(f"Vous avez trouvé le mot! {motMystere}")
                break
        else: 
            x = x - 1
            print(f"Essayez encore! Il vous reste {x} essais.")

print(x)
    
    
