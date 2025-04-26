import time

def jugar_adivinanza(numero_secreto, intentos_restantes, tiempo_inicio):
    if intentos_restantes == 0:
        print("¡Sin más oportunidades! El número correcto era:", numero_secreto)
        return

    intento = int(input("¿Cuál es tu suposición? "))  
    
    if intento == numero_secreto:
        tiempo_total = time.time() - tiempo_inicio
        print("🎉 ¡Correcto! Has adivinado el número.")
        print(f"⏱️ Lo lograste en {tiempo_total:.2f} segundos.")
        return
    elif intento < numero_secreto:
        print("Muy bajo. 🚫")
    else:
        print("Muy alto. 🚫")
    
    print(f"Intentos restantes: {intentos_restantes - 1}")
    jugar_adivinanza(numero_secreto, intentos_restantes - 1, tiempo_inicio)

numero_a_adivinar = 80

print("🔢 Bienvenido al reto: ¿Puedes adivinar el número?")
print("Pista: Está entre 1 y 100.")
print("Tienes 5 oportunidades. ¡A por ello!")

inicio_tiempo = time.time()

jugar_adivinanza(numero_a_adivinar, 5, inicio_tiempo)