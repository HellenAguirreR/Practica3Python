class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio} - Año: {self.año}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        return productos_filtrados

if __name__ == "__main__":
    catalogo = Catalogo()

    producto1 = Producto("Batería", 100, 2022)
    producto2 = Producto("Filtro de aceite", 15, 2021)
    producto3 = Producto("Pastillas de freno", 50, 2022)

    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    print("Todos los productos en el catálogo:")
    catalogo.mostrar_productos()

    año_a_filtrar = 2022
    print(f"\nProductos filtrados por año {año_a_filtrar}:")
    productos_filtrados = catalogo.filtrar_por_año(año_a_filtrar)
    for producto in productos_filtrados:
        print(producto)
