# Definir Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters para cada atributo
    def get_id_producto(self):
        return self.id_producto

    def set_id_producto(self, id_producto):
        self.id_producto = id_producto

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"


# Definir Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: Producto ya existe.")
            self.productos[producto.id_producto].cantidad += producto.cantidad
        else:
            self.productos[producto.id_producto] = producto
            print("Producto ha sido agregado al Inventario")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con Id {id_producto} ha sido eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print(f"Producto con ID {id_producto} ha sido actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrado = False
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)
                encontrado = True
        if not encontrado:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario esta vacio.")
        else:
            for producto in self.productos.values():
                print(producto)


# Menu interactivo
def menu():
    inventario = Inventario()

    while True:
        print("=" * 50)
        print("Sistema de Gestion de Inventarios".center(50))
        print("=" * 50)
        print(f"{'Opcion':<20}{'Descripcion'}")
        print("-" * 50)
        print(f"{'1':<20}{'Añadir Producto'}")
        print(f"{'2':<20}{'Eliminar Producto'}")
        print(f"{'3':<20}{'Actualizar Producto'}")
        print(f"{'4':<20}{'Buscar Producto'}")
        print(f"{'5':<20}{'Mostrar Inventario'}")
        print(f"{'6':<20}{'Salir'}")
        print("-" * 50)

        opcion = input("Selecciona una opcion (1-6): ")

        if opcion == '1':
            try:
                id_producto = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: Por favor ingrese valores validos.")

        elif opcion == '2':
            try:
                id_producto = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("Error: Por favor ingrese un ID válido.")

        elif opcion == '3':
            try:
                id_producto = int(input("Ingrese el ID del producto a actualizar: "))
                cantidad = input("Ingrese la nueva cantidad (deje vacio para no cambiar): ")
                precio = input("Ingrese el nuevo precio (deje vacio para no cambiar): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("Error: Por favor ingrese valores validos.")

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            print("¡Hasta la Proxima!")
            break

        else:
            print("Opcion no valida, por favor selecciona una opcion entre 1 y 6.")


if __name__ == '__main__':
    menu()
