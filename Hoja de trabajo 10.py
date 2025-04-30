# Veterinaria 
class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
class Perro(Animal):
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self.raza = raza
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Raza: {self.raza}")
        print(f"Tipo: Perro")
class Gato(Animal):
    def __init__(self, nombre, edad, peso, color):
        super().__init__(nombre, edad, peso)
        self.color = color
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Color: {self.color}")
        print(f"Tipo: Gato")
class Ave(Animal):
    def __init__(self, nombre, edad, peso, tipo_ave):
        super().__init__(nombre, edad, peso)
        self.tipo_ave = tipo_ave
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de ave: {self.tipo_ave}")
class Reptil(Animal):
    def __init__(self, nombre, edad, peso, tipo_reptil):
        super().__init__(nombre, edad, peso)
        self.tipo_reptil = tipo_reptil
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de reptil: {self.tipo_reptil}")

#Institución 
class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"DNI: {self.dni}")
class Estudiante(Persona):
    def __init__(self, nombre, edad, dni, carrera):
        super().__init__(nombre, edad, dni)
        self.carrera = carrera
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Carrera: {self.carrera}")
        print(f"Tipo: Estudiante")
class Profesor(Persona):
    def __init__(self, nombre, edad, dni, materia):
        super().__init__(nombre, edad, dni)
        self.materia = materia
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Materia: {self.materia}")
        print(f"Tipo: Profesor")
class Administrativo(Persona):
    def __init__(self, nombre, edad, dni, departamento):
        super().__init__(nombre, edad, dni)
        self.departamento = departamento
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Departamento: {self.departamento}")
        print(f"Tipo: Administrativo")
