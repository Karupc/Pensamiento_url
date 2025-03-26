'''Ejercicio 1'''
for i in range(1,11):
    if i% 2!=0:
        print(i)
'''Ejercicio 2'''
b=1
while b<11:
    if b % 2!= 0:
        print
    b+=1
'''Escenario 1'''
while True:
    pal = input("Ingrese una palabra: ")
    if pal.lower()== "chupacabra":
        print("¡Has dejado el bucle con éxito!")
        break 
'''Escenario 2'''
pal = input("Ingrese una palabra: ").upper()
vo="AEIOU"
for let in pal:
    if let in vo:
        continue
    print(let)