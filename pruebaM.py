class Producto:
    def _init_(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.margen_de_venta = margen_de_venta
        self.precio_de_venta = self.calcular_precio_de_venta()

    def calcular_precio_de_venta(self):
        return self.costo / (1 - self.margen_de_venta)


class RegistroProductos:
    def _init_(self):
        self.productos = {}

    def registrar_producto(self, producto):
        if producto.id not in self.productos:
            self.productos[producto.id] = producto
        else:
            print("Ya existe un producto con el mismo ID. No se pudo registrar.")

    def imprimir_productos(self):
        print("Listado de Productos de Aseo Personal:")
        for id, producto in self.productos.items():
            print(f"ID: {producto.id}")
            print(f"Nombre: {producto.nombre}")
            print(f"Descripción: {producto.descripcion}")
            print(f"Costo: ${producto.costo:,.2f} COP")
            print(f"Cantidad: {producto.cantidad}")
            print(f"Precio de Venta: ${producto.precio_de_venta:,.2f} COP")
            print()


if _name_ == "_main_":
    registro = RegistroProductos()

    producto1 = Producto(1, "Champú", "Champú suave para cabello", 15000, 50, 0.15)
    registro.registrar_producto(producto1)

    producto2 = Producto(2, "Jabón", "Jabón dove", 3000, 100, 0.1)
    registro.registrar_producto(producto2)

    producto3 = Producto(3, "Crema Dental", "Crema dental Colgate", 5000, 75, 0.2)
    registro.registrar_producto(producto3)

    registro.imprimir_productos()