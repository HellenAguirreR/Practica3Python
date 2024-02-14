class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = None

    def display(self):
        print(f"Información del estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas is not None:
            print(f"Notas: {', '.join(map(str, self.notas))}")

    def set_edad(self, edad):
        self.edad = edad

    def set_notas(self, notas):
        self.notas = notas

try:
    nombre = input("Ingrese el nombre del estudiante: ")
    numero_registro = input("Ingrese el número de registro del estudiante: ")

    alumno = Alumno(nombre, numero_registro)

    edad = int(input("Ingrese la edad del estudiante: "))
    alumno.set_edad(edad)

    notas_str = input("Ingrese las notas del estudiante separadas por comas: ")
    notas = [float(nota.strip()) for nota in notas_str.split(',')]
    alumno.set_notas(notas)

    alumno.display()
except ValueError:
    print("Error: Ingrese valores numéricos para la edad y las notas.")
except Exception as e:
    print(f"Error inesperado: {e}")
