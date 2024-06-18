travel = "Jean and her family recently traveled to Boston, Massachusetts, one of America's oldest colonial cities. Boston is rich in history and local personality. During their visit, Jean and her family appreciated learning about Boston's role during the American Revolution."

L = travel.split(". ")
print(f"Voici les différentes phrases:\n{L}")

a = travel.replace(",", "")
L2 = a.split(". ")
print(f"Voici les différentes phrases sans ponctuation:\n{L2}")

x = a.split()
mots = []
for mot in x:
    if mot not in mots:
        mots.append(mot)
    else:
        pass

lenght = len(mots)
liste = sorted(mots)

print(f"Il y a {lenght} mots dans ces phrases. Mots dans l'ordre alphabétique:\n{liste}")
    
    
