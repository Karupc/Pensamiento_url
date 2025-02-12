print("CONVERSOR DE NÚMEROS ROMANOS")
num = int(input("Escriba un número entre 1-9 para convertirlo a romanos: "))
resultado = ''
if num <=3:
   resultado = num * "I"
   print("En números romanos es: ", resultado)
elif num == 4:
    print("En números romanos es: IV")
elif num >= 5 and num<=8:
    print("En números romanos es: " + "V" + (int(num-5)*"I"))
elif num == 9:
    print("En números romanos es: IX")
elif num == 10:
    print("No está dentro del rango")