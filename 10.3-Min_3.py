ch = input("Entrer une chaîne de caractères: ")
x = ch.split()
mots = []
for mot in x:
    if len(mot) > 3:
        mots.append(mot)
    else:
        pass

print(" ".join(mots))