# mifunciones.py

import random

def generar_numeros_aleatorios():
    return [random.randint(0, 100) for _ in range(20)]

def mostrar_lista(lista):
    print("Lista generada:", lista)

def ordenar_y_mostrar(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:", lista_ordenada)

# main.py

from mifunciones import generar_numeros_aleatorios, mostrar_lista, ordenar_y_mostrar

if __name__ == "__main__":
    # Generar la lista de 20 números aleatorios
    numeros_aleatorios = generar_numeros_aleatorios()

    # Mostrar la lista original
    mostrar_lista(numeros_aleatorios)

    # Ordenar y mostrar la lista ordenada
    ordenar_y_mostrar(numeros_aleatorios)
