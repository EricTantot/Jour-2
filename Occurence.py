def nombre_chiffres(nombre, chiffre):
    x = 0
    for char in nombre:
        if char == chiffre:
            x = x + 1
        else : 
            pass

    return x

nombre = input("Nombre: ")
chiffre = input("Chiffre: ")

output = nombre_chiffres(nombre, chiffre)

print(output)