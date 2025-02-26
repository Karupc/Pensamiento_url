num= input("Ingrese un número de 5 dígitos: ")
di1, di2, di3, di4, di5 = int(num[0]), int(num[1]), int(num[2]), int(num[3]), int(num[4])
dig = [di1, di2, di3, di4, di5]
print("El orden es el siguiente: ")
if dig[0] > dig[1]: dig[0], dig[1] = dig[1], dig[0]
if dig[1] > dig[2]: dig[1], dig[2] = dig[2], dig[1]
if dig[2] > dig[3]: dig[2], dig[3] = dig[3], dig[2]
if dig[3] > dig[4]: dig[3], dig[4] = dig[4], dig[3]

if dig[0] > dig[1]: dig[0], dig[1] = dig[1], dig[0]
if dig[1] > dig[2]: dig[1], dig[2] = dig[2], dig[1]
if dig[2] > dig[3]: dig[2], dig[3] = dig[3], dig[2]

if dig[0] > dig[1]: dig[0], dig[1] = dig[1], dig[0]
if dig[1] > dig[2]: dig[1], dig[2] = dig[2], dig[1]

if dig[0] > dig[1]: dig[0], dig[1] = dig[1], dig[0]
print("Números en orden ascendente:", dig[0], dig[1], dig[2], dig[3], dig[4])
print("Números en orden descendente:", dig[4], dig[3], dig[2], dig[1], dig[0])