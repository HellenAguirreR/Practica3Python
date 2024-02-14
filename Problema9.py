# operaciones.py

def suma(num1, num2):
    try:
        resultado = float(num1) + float(num2)
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def resta(num1, num2):
    try:
        resultado = float(num1) - float(num2)
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def producto(num1, num2):
    try:
        resultado = float(num1) * float(num2)
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def division(num1, num2):
    try:
        num2 = float(num2)
        if num2 == 0:
            raise ZeroDivisionError
        resultado = float(num1) / num2
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero"

# calculos.py

from operaciones import suma, resta, producto, division

if __name__ == "__main__":
    # Ejemplo de uso
    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")

    print("Suma:", suma(num1, num2))
    print("Resta:", resta(num1, num2))
    print("Producto:", producto(num1, num2))
    print("División:", division(num1, num2))
