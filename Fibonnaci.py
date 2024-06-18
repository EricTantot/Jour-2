n = int(input("Termes: "))

out = []

x = 0
y = 1
out.append(f"{x}, ")
out.append(f"{y}, ")

for i in range(n):
    a = x + y
    out.append(f"{a}, ")
    x = y
    y = a

print("".join(out))
