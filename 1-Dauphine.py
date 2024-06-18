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

print(c1)


"""
1.Quelles sont les variables locales à la fonction mystere()?
ch2 et i

2. Après l'exécution du programme, si l'utilisateur saisit au clavier Le sens de la vie, quelle sera la valeur référencée par la variable c1?
sse

3. À la place de l'instruction c2 = mystere(c, 14, len(c), 1)), proposer une unique instruction permettant d'affecter la même valeur à c2 sans faire appel à la fonction
mystere().





"""