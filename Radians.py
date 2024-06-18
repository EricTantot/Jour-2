def radian(degrés, minutes, secondes):
    output = degrés + (minutes+secondes/60)/60
    return output

degrés = int(input("Degrés: "))
minutes = int(input("Minutes: "))
secondes = int(input("Secondes: "))

out = radian(degrés, minutes, secondes)
print(out)