import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio**2
        return area

try:
    radio = float(input("Ingrese el radio del círculo: "))
    mi_circulo = Circulo(radio)
    area_circulo = mi_circulo.calcular_area()
    print(f"El área del círculo con radio {radio} es: {area_circulo:.2f}")
except ValueError:
    print("Error: Ingrese un valor numérico para el radio.")
except Exception as e:
    print(f"Error inesperado: {e}")
