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

