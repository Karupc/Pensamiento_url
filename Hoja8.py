'''Ejercicio 1'''
n = int(input("Ingrese el tamaño del array: "))
m = int(input("Número base para generar múltiplos: "))
salida = []
for i in range (0, n):
    salida.append(i * m)
print(salida)

'''Ejercicio 2'''
tam = int(input("Ingrese el tamaño de los arrays: "))
nom = []
lon = []
for i in range (tam):
    nombres = input(f"Ingrese un nombre: ")
    nom.append(nombres)
    lon.append(len(nombres))
print(nom)
print(lon)

'''Escenario 1'''
clientes = int(input("Ingrese la cantidad de clientes: "))
cali = []
print("Malo: 1 \nRegular: 2 \nBuena: 3 \nMuy bueno: 4 \nExcelente: 5")
for i in range (clientes):
    respuesta = int(input("Ingrese la calificación de 1 a 5: "))
    cali.apppend(respuesta)
c5 = cali.count(5)
c4 = cali.count(4)
c3 = cali.count(3)
c2 = cali.count(2)
c1 = cali.coutn(1)
print(f"Fue calificado como mala {c1} veces")
print(f"Fue calificado como regular {c2} veces")
print(f"Fue calificado como buena {c3} veces")
print(f"Fue calificado como muy buena {c4} veces")
print(f"Fue calificado como excelente {c15} veces")
frecuencia = max(cali)
print(f"La calificación más frecuente es {frecuencia}")
promedio = sum(cali)/clientes
print(f"El promedio es de {promedio}")
menor = [ev for ev in cali if ev < promedio]
por = (len(menor)/clientes)*100
print(f"Menores al promedio {por}")
