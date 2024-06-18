def rendu(somme):
    while somme > 0:
        if somme - 100 > 0:
            somme = somme - 100
            e100 = 0
            e100 = e100 + 1
        elif somme - 50 > 0:
            somme = somme - 50
            e50 = 0
            e50 = e50 + 1
        elif somme - 20 > 0:
            somme = somme - 20
            e20 = 0
            e20 = e20 + 1
        elif somme - 10 > 0: 
            somme = somme - 10
            e10 = 0
            e10 = e10 + 1
        elif somme - 5 > 0:
            somme = somme - 10
            e5 = 0
            e5 = e5 + 1
        elif somme - 2 > 0:
            somme = somme - 2
            e2 = 0
            e2 = e2 + 1
        elif somme - 1 > 0:
            somme = somme - 1
            e1 = 0
            e1 = e1 + 1
        elif somme - 0.5 > 0:
            somme = somme - 0.5
            e05 = 0
            e05 = e05 + 1
        elif somme - 0.2 > 0:
            somme = somme - 0.2
            e02 = 0
            e02 = e02 + 1
        elif somme - 0.1 > 0:
            somme = somme - 0.1
            e01 = 0
            e01 = e01 + 1
        elif somme - 0.05 > 0:
            somme = somme - 0.05
            e005 = 0
            e005 = e005 + 1
        elif somme - 0.02 > 0:
            somme = somme - 0.02
            e002 = 0
            e002 = e002 + 1
        elif somme - 0.01 > 0:
            somme = somme - 0.01 
            e001 = 0
            e001 = e001 + 1
        else : 
            pass
    print(f"""100€: {e100}
50€: {e50}
20€: {e20}
10€: {e10}
5€: {e5}
2€: {e2}
1€: {e1}
0.50€: {e05}
0.20€: {e02}
0.10€: {e01}
0.05€: {e005}
0.02€: {e002}
0.01€: {e001}
          """)

prix = float(input("Entrer une somme: "))
rendu(prix)