saldo = 3000
inten = 0

while True:
    print("Saldo actual: Q", saldo)
    print("Escriba 0 si quiere salir")
    monto = int(input("Ingrese monto a retirar: "))
    
    if monto == 0:
        print("Gracias por usar el cajero. Adiós.")
        break
    
    if monto > saldo:
        inten += 1
        print("Saldo insuficiente. Intentos restantes:", 3 - inten)
        if inten >= 3:
            print("Demasiados intentos no válidos. El programa terminará.")
            break
    else:
        saldo = saldo - monto
        print("Retiro exitoso. Nuevo saldo: Q", saldo)
        if saldo == 0:
            print("Saldo agotado. Adiós.")
            break