'''1'''
import math
class Cai:
    def __init__(self, alt, gra):
        self.alt = alt
        self.gra = gra
    def cal(self):
        if self.alt < 0:
            print("Altura no puede ser negativa")
            return
        if self.gra == 0:
            print("Gravedad no puede ser cero")
            return
        t = math.sqrt(2 * self.alt / self.gra)
        print("Tiempo:", t)
'''2'''
import math
class Cal:
    def rai(self, num):
        if num < 0:
            print("Raíz no válida")
        else:
            print("Raíz:", math.sqrt(num))
    def pot(self, bas, exp):
        print("Pot:", math.pow(bas, exp))
    def log(self, num):
        if num <= 0:
            print("Log no válido")
        else:
            print("Log:", math.log(num))
    def fac(self, num):
        if num < 0 or not float(num).is_integer():
            print("Factorial no válido")
        else:
            print("Fac:", math.factorial(int(num)))
