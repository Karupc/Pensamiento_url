entrada = input("Ingrese una oración: ")
pal = entrada.split()
print("Palabra del inicio: ", {pal[0]}, "Palabra del final: ", {pal[-1]})

espacios = input("Ingresa una oración: ")
print(" ".join(espacios.split()))

mail = input("Ingrese correo electrónico: ")
dom = (mail.split("@")[-1])
print(dom)

archivo = input("Ingrese el tipo de archivo: ")
print(archivo.endswith("pdf"))

contrario = input("Ingrese una oración: ")
print(" ".join(contrario.split()[::-1]))

palabra = input("Escriba que desea: ").lower()
if "poema" in palabra:
    print("Mi vida es como un erial, flor que toco se deshoja; que en mi camino fatal alguien va sembrando el mal para que yo lo recoja.")
elif "canción" in palabra:
    print("Me complace amarte, disfruto acariciarte, ponerte a dormir, es escalofriante tenerte de frente hacerte sonreir...")
elif "refrán" in palabra:
    print("El que escupe para arriba en la cara le cae.")
elif "chiste" in palabra:
    print("Si car es carro y men es hombre entonces Carmen es un transformer...")
elif "adivinanza" in palabra:
    print("Es una planta con una flor, que gira y gira buscando el sol. Respuesta: El girasol.")