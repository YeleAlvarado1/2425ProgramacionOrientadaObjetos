import os

# Clase Producto Representa un producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único para cada producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible en inventario
        self.precio = precio  # Precio del producto

    # Metodo para mostrar la informacion del producto de forma amigable
    def __str__(self):
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

# Clase Inventario Gestiona el inventario de productos en memoria y archivo
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo  # Archivo donde se guarda el inventario
        self.productos = self.cargar_inventario()  # Carga el inventario desde el archivo al diccionario

    def cargar_inventario(self):
        productos = {}
        if os.path.exists(self.archivo):  # Verifica si el archivo existe
            print(f"Archivo {self.archivo} encontrado, cargando inventario...")  # Mensaje para confirmar
            try:
                with open(self.archivo, 'r') as file:
                    lineas = file.readlines()
                    for linea in lineas:
                        datos = linea.strip().split(',')
                        if len(datos) == 4:
                            id_producto, nombre, cantidad, precio = datos
                            productos[int(id_producto)] = Producto(int(id_producto), nombre, int(cantidad),
                                                                   float(precio))
            except Exception as e:
                print(f"Error al cargar el inventario: {e}")
        else:
            print(
                f"El archivo {self.archivo} no existe. Se creará al agregar productos.")  # Mensaje si el archivo no existe
        return productos

    def guardar_inventario(self):
        #Guarda todos los productos del diccionario al archivo
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos.values():
                    file.write(f"{producto.id_producto},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            print("El inventario se ha guardado exitosamente en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def modificar_producto(self, producto, accion):
        #Permite agregar, eliminar o actualizar productos"""
        if accion == "agregar":
            if producto.id_producto in self.productos:
                print("Error: Producto ya existe.")  # Si el producto ya existe, actualiza la cantidad
                self.productos[producto.id_producto].cantidad += producto.cantidad
            else:
                self.productos[producto.id_producto] = producto  # Agrega el producto nuevo
                print("Producto ha sido agregado al Inventario")
        elif accion == "eliminar":
            if producto.id_producto in self.productos:
                del self.productos[producto.id_producto]  # Elimina el producto por ID
                print(f"Producto con Id {producto.id_producto} ha sido eliminado.")
            else:
                print("Error: Producto no encontrado.")
        elif accion == "actualizar":
            if producto.id_producto in self.productos:
                # Actualiza la cantidad y el precio del producto
                self.productos[producto.id_producto].cantidad = producto.cantidad
                self.productos[producto.id_producto].precio = producto.precio
                print(f"Producto con ID {producto.id_producto} ha sido actualizado.")
            else:
                print("Error: Producto no encontrado.")

        # Guarda el inventario después de cada modificación en memoria
        self.guardar_inventario()

    def buscar_producto(self, nombre):
        #Busca un producto por nombre
        encontrado = False
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)  # Muestra el producto encontrado
                encontrado = True
        if not encontrado:
            print("No se encontraron productos con ese nombre.")  # Si no se encuentra el producto

    def mostrar_inventario(self):
        #Muestra todos los productos en el inventario
        if not self.productos:
            print("El inventario se encuentra vacio.")
        else:
            for producto in self.productos.values():
                print(producto)  # Muestra cada producto en el inventario

# Funcion que muestra el menu y permite interactuar con el sistema de inventarios
def menu():
    inventario = Inventario()  # Se crea una instancia de la clase Inventario

    while True:
        # Imprime el menu con opciones
        print("=" * 50)
        print("Sistema de Gestion de Inventarios".center(50))
        print("=" * 50)
        print(f"{'Opcion':<20}{'Descripcion'}")
        print("-" * 50)
        print(f"{'1':<10}{'Añadir Producto'}")
        print(f"{'2':<10}{'Eliminar Producto'}")
        print(f"{'3':<10}{'Actualizar Producto'}")
        print(f"{'4':<10}{'Buscar Producto'}")
        print(f"{'5':<10}{'Mostrar Inventario'}")
        print(f"{'6':<10}{'Salir'}")
        print("-" * 50)

        opcion = input("Selecciona una opcion (1-6): ")  # Solicita la opcion del usuario

        if opcion == '1':  # Opción para añadir producto
            try:
                id_producto = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)  # Crea el producto
                inventario.modificar_producto(producto, "agregar")  # Agrega el producto al inventario
            except ValueError:
                print("Error: Por favor ingrese valores válidos.")  # Captura errores si los valores no son válidos

        elif opcion == '2':  # Opción para eliminar producto
            try:
                id_producto = int(input("Ingrese el ID del producto a eliminar: "))
                producto = Producto(id_producto, "", 0, 0.0)  # Crea un producto solo con ID
                inventario.modificar_producto(producto, "eliminar")  # Elimina el producto
            except ValueError:
                print("Error: Por favor ingrese un ID válido.")  # Captura errores en la entrada de datos

        elif opcion == '3':  # Opción para actualizar producto
            try:
                id_producto = int(input("Ingrese el ID del producto a actualizar: "))
                cantidad = input("Ingrese la nueva cantidad (deje vacío para no cambiar): ")
                precio = input("Ingrese el nuevo precio (deje vacío para no cambiar): ")

                cantidad = int(cantidad) if cantidad else None  # Si no se ingresa cantidad, la dejamos como None
                precio = float(precio) if precio else None  # Si no se ingresa precio, lo dejamos como None

                # Verifica si al menos uno de los campos fue actualizado
                if cantidad is None and precio is None:
                    print("Debe proporcionar al menos una nueva cantidad o precio.")
                else:
                    # Se asegura de que el id_producto siempre sea consistente al actualizar
                    producto = Producto(id_producto, "", cantidad if cantidad is not None else 0,
                                        precio if precio is not None else 0.0)
                    inventario.modificar_producto(producto, "actualizar")  # Actualiza el producto
            except ValueError:
                print("Error: Por favor ingrese valores válidos.")  # Captura errores en la entrada de datos

        elif opcion == '4':  # Opción para buscar producto
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':  # Opción para salir
            print("Gracias por usar nuestro Sistema de Gestion de Inventarios¡Hasta la próxima!")  # Mensaje de despedida
            break  # Sale del bucle y termina el programa

        else:
            print("Opción no válida, por favor selecciona una opción entre 1 y 6.")  # Opción inválida

# El bloque principal que ejecuta el programa
if __name__ == '__main__':
    menu()  # Llama al menú para ejecutar el sistema de inventarios

