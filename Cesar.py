def decrypt(message):
    out = []
    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for char in message :
        if char in x:
            index = x.index(char)
            new = index + 3
            if new > 26 :
                inverse = -(len(x)-index)
                new = inverse + 3
            else : 
                pass
            result = x[new]
            out.append(result)
        else : 
            pass
    return("".join(out))

a = input("Entrer un message: ")
b = decrypt(a)
print(b)
