def obtener_calificaciones():
    while True:
        try:
            entrada = input("Ingrese una lista de calificaciones separadas por comas: ")
            calificaciones_str = entrada.split(',')
            calificaciones_int = [int(calificacion.strip()) for calificacion in calificaciones_str]
            return calificaciones_int
        except ValueError as ve:
            print(f"Error: {ve}. Asegúrese de ingresar valores numéricos.")
        except Exception as e:
            print(f"Error inesperado: {e}")

def main():
    calificaciones = obtener_calificaciones()

    print("\nCalificaciones ingresadas:")
    for calificacion in calificaciones:
        print(calificacion)

if __name__ == "__main__":
    main()
