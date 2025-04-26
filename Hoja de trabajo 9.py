

# 1
def par_o_impar(numero):
    if numero % 2 == 0: 
        print("Es par")
    else:
        print("Es impar")

valor = int(input("Ingrese un número: "))
par_o_impar(valor)

# 2
def sumar_lista(numeros):
    return sum(numeros)

entrada_numeros = input("Ingrese una lista de números separados por una coma: ")
lista_numeros = [int(x) for x in entrada_numeros.split(',')]
print("La suma es: ", sumar_lista(lista_numeros))

# 3
def cuenta_regresiva(numero):
    if numero >= 0:
        print(numero)
        cuenta_regresiva(numero - 1)

inicio = int(input("Ingrese el número para iniciar la cuenta regresiva: "))
cuenta_regresiva(inicio)

# 4
def contar_ascendente(limite, actual=1):
    if actual > limite:
        return
    print(actual)
    contar_ascendente(limite, actual + 1)

tope = int(input("Ingrese el número tope: "))
contar_ascendente(tope)

# 5
def suma_hasta_uno(numero):
    if numero == 1:
        return numero
    return numero + suma_hasta_uno(numero - 1)

limite_suma = int(input("Ingresa el número tope para la suma: "))
print("La suma es: ", suma_hasta_uno(limite_suma))

# 6
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1 
    return numero * factorial(numero - 1)

numero_fact = int(input("Ingresa un número para calcular el factorial: "))
print(f"El factorial de {numero_fact} es: {factorial(numero_fact)}")

# 7
def minimo(lista_numeros):
    if not lista_numeros[1:]:
        return lista_numeros[0]
    menor = minimo(lista_numeros[1:])
    return lista_numeros[0] if lista_numeros[0] < menor else menor

entrada_valores = input("Ingresa números separados por coma: ")
lista_valores = [int(x) for x in entrada_valores.split(',')]
print("El número mínimo es:", minimo(lista_valores))