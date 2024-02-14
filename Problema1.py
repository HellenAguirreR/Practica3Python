def obtener_fraccion():
    while True:
        try:
            entrada = input("Ingrese una fracción en formato X/Y (donde X e Y son números enteros y X <= Y, Y != 0): ")
            x, y = map(int, entrada.split('/'))

            if x <= 0 or y <= 0 or x > y:
                raise ValueError("X y Y deben ser números enteros, X <= Y y Y != 0")

            return x, y

        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError:
            print("Error: Y no puede ser igual a 0")

def calcular_porcentaje(x, y):
    porcentaje = (x / y) * 100

    if porcentaje < 1:
        return 'E'
    elif porcentaje > 99:
        return 'F'
    else:
        return f"{round(porcentaje)}%"

def main():
    while True:
        try:
            numerador, denominador = obtener_fraccion()
            resultado = calcular_porcentaje(numerador, denominador)
            print(f"La cantidad de combustible en el tanque es: {resultado}")
            break
        except KeyboardInterrupt:
            print("\n¡Programa interrumpido!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
