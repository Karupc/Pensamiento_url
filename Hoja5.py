cona = int(input("Ingrese el consumo de agua en metros cúbicos: "))
if cona < 15:
    print("La tarifa es de Q", cona*5)
elif cona >= 15 and cona <= 30:
    per = int(input("Ingrese cantidad de habitantes: "))
    if per > 3:
        print("La tarifa es de Q", cona*4)
    elif per == 3:
        print("La tarifa es de Q", cona*4.5)
    else:
        print("La tarifa es de Q", cona*5)
elif cona > 30:
    per = int(input("Ingrese cantidad de habitantes: "))
    if per > 5:
        print("La tarifa es de Q", cona*3.5)
    elif per %2 == 0:
        print("La tarifa es de Q", cona*4)
    else:
        print("La tarifa es de Q", cona*4.2)
        

avehi = int(input("Ingrese el año de su vehículo: "))
if avehi > 2001:
    plac = int(input("Ingrese la placa del vehículo: "))
    if plac % 10 == 0 or plac % 10 == 2 or plac % 10 == 4 or plac % 10 ==6 or plac % 10 == 8:
        print("No circula los lunes")
    elif plac % 10 == 1 or plac % 10 == 3 or plac % 10 ==5 or plac % 10 == 7 or plac % 10 == 9:
        print("Circula los viernes")
if avehi % 2 == 0: 
    print("Restricción adicional, los sábados circula hasta medio día.")
if avehi < 2001:
    print("ADVETENCIA, Debe darle mantenimiento obligatorio a su vehículo.")