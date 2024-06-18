def mystere(ch, n, m, p):
    ch2 = ""
    i = n
    while i < m:
        ch2 = ch2 + ch[i]
        i = i + p
    return ch2
c = input()
c1 = mystere(c, 3, 10, 3)
c2 = mystere(c, 14, len(c), 1)
ch3 = (c )

print(c1)


"""
1.Quelles sont les variables locales à la fonction mystere()?
ch2 et i

2. Après l'exécution du programme, si l'utilisateur saisit au clavier Le sens de la vie, quelle sera la valeur référencée par la variable c1?
sse

3. À la place de l'instruction c2 = mystere(c, 14, len(c), 1)), proposer une unique instruction permettant d'affecter la même valeur à c2 sans faire appel à la fonction
mystere().


4. Étant donnée une variable L référençant la liste [7, 3, -2, 10, 0], quelle instruction doit-on exécuter pour modifier L en triant ses valeurs par ordre croissant ?
.sort()

5. . Quelle est la valeur référencée par la liste P après l'exécution du programme ci-dessous ? """
P = [[4,7,8], [], [10,0]]
for i in range(len(P)):
    P[i].append(i + 1)
"""
P = [[4,7,8,1], [2], [10,0,3]]

6. Quelles sont les instructions qui permettent de créer, dans le répertoire de travail courant, un fichier dont le nom est new.txt contenant sur la première ligne Bonne Année et sur la seconde ligne 2022?


"""