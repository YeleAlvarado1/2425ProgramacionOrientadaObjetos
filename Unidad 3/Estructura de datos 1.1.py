import os

# Clase Producto Representa un producto en el inventario.
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Inicializa el producto con los atributos id, nombre, cantidad y precio
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Metodo que permite imprimir el producto de forma entendible
    def __str__(self):
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

# Clase Inventario Gestiona el inventario de productos en un archivo de texto.
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        # Se inicializa el archivo donde se guarda el inventario y se carga el inventario desde el archivo.
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        # Metodo que carga los productos desde el archivo de inventario si existe.
        productos = {}
        if os.path.exists(self.archivo):  # Verifica si el archivo existe
            try:
                with open(self.archivo, 'r') as file:
                    lineas = file.readlines()
                    for linea in lineas:
                        # Separa los datos por comas y los convierte a los tipos adecuados
                        datos = linea.strip().split(',')
                        if len(datos) == 4:
                            id_producto, nombre, cantidad, precio = datos
                            productos[int(id_producto)] = Producto(int(id_producto), nombre, int(cantidad), float(precio))
            except Exception as e:
                print(f"Error al cargar el inventario: {e}")  # Captura cualquier error al leer el archivo
        return productos  # Devuelve el inventario cargado

    def guardar_inventario(self):
        # Metodo que guarda todos los productos en el archivo de inventario.
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos.values():
                    file.write(f"{producto.id_producto},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            print("El inventario se ha guardado exitosamente.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")  # Captura errores al guardar el archivo

    def modificar_producto(self, producto, accion):
        # Metodo que permite agregar, eliminar o actualizar un producto dependiendo de la accion indicada.
        if accion == "agregar":
            if producto.id_producto in self.productos:
                print("Error: Producto ya existe.")  # Si el producto ya existe, solo actualiza la cantidad
                self.productos[producto.id_producto].cantidad += producto.cantidad
            else:
                self.productos[producto.id_producto] = producto  # Agrega el producto nuevo al inventario
                print("Producto ha sido agregado al Inventario")
        elif accion == "eliminar":
            if producto.id_producto in self.productos:
                del self.productos[producto.id_producto]  # Elimina el producto por su ID
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

        # Guarda el inventario después de cada modificación
        self.guardar_inventario()

    def buscar_producto(self, nombre):
        # Metodo que busca un producto por su nombre (parcial o completo).
        encontrado = False
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)  # Imprime el producto si encuentra una coincidencia
                encontrado = True
        if not encontrado:
            print("No se encontraron productos con ese nombre.")  # Si no se encuentra el producto

    def mostrar_inventario(self):
        # Metodo que muestra todos los productos del inventario.
        if not self.productos:
            print("El inventario se encuentra vacio.")  # Si no hay productos, avisa al usuario
        else:
            for producto in self.productos.values():
                print(producto)  # Muestra cada producto en el inventario


# Menú interactivo para que el usuario realice las acciones en el inventario.
def menu():
    inventario = Inventario()  # Instanciamos la clase Inventario

    while True:
        # Imprime el menú de opciones para el usuario
        print("=" * 50)
        print("Sistema de Gestion de Inventarios".center(50))  # Título del sistema
        print("=" * 50)
        print(f"{'Opcion':<20}{'Descripcion'}")  # Formato de las opciones
        print("-" * 50)
        print(f"{'1':<10}{'Añadir Producto'}")
        print(f"{'2':<10}{'Eliminar Producto'}")
        print(f"{'3':<10}{'Actualizar Producto'}")
        print(f"{'4':<10}{'Buscar Producto'}")
        print(f"{'5':<10}{'Mostrar Inventario'}")
        print(f"{'6':<10}{'Salir'}")
        print("-" * 50)

        opcion = input("Selecciona una opcion (1-6): ")  # Entrada de la opciOn seleccionada

        if opcion == '1':  # Añadir Producto
            try:
                id_producto = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)  # Crea el nuevo producto
                inventario.modificar_producto(producto, "agregar")  # Llama a modificar_producto para agregarlo
            except ValueError:
                print("Error: Por favor ingrese valores validos.")  # Captura errores en la entrada de datos

        elif opcion == '2':  # Elimina Producto
            try:
                id_producto = int(input("Ingrese el ID del producto a eliminar: "))
                producto = Producto(id_producto, "", 0, 0.0)  # Crea un producto con solo el id
                inventario.modificar_producto(producto, "eliminar")  # Llama a modificar_producto para eliminarlo
            except ValueError:
                print("Error: Por favor ingrese un ID valido.")  # Captura errores en la entrada de datos

        elif opcion == '3':  # Actualizar Producto
            try:
                id_producto = int(input("Ingrese el ID del producto a actualizar: "))
                cantidad = input("Ingrese la nueva cantidad (deje vacio para no cambiar): ")
                precio = input("Ingrese el nuevo precio (deje vacio para no cambiar): ")

                cantidad = int(cantidad) if cantidad else None  # Si no se ingresa cantidad, se deja como None
                precio = float(precio) if precio else None  # Si no se ingresa precio, se deja como None

                # Verifica que al menos uno de los campos no sea None para realizar la actualización
                if cantidad is None and precio is None:
                    print("Debe proporcionar al menos una nueva cantidad o precio.")  # No se puede actualizar sin datos
                else:
                    producto = Producto(id_producto, "", cantidad if cantidad is not None else 0,
                                        precio if precio is not None else 0.0)
                    inventario.modificar_producto(producto, "actualizar")  # Llama a modificar_producto para actualizarlo
            except ValueError:
                print("Error: Por favor ingrese valores validos.")  # Captura errores en la entrada de datos

        elif opcion == '4':  # Buscar Producto
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)  # Llama a buscar_producto para buscar el producto

        elif opcion == '5':  # Mostrar Inventario
            inventario.mostrar_inventario()  # Llama a mostrar_inventario para imprimir todos los productos

        elif opcion == '6':  # Salir del programa
            print("¡Hasta la proxima!")  # Mensaje de despedida
            break  # Sale del bucle y termina el programa

        else:
            print("Opcion no valida, por favor selecciona una opcion entre 1 y 6.")  # Captura de opciones inválidas


# El bloque principal que ejecuta el programa
if __name__ == '__main__':
    menu()  # Llama al menu para ejecutar el sistema de inventarios
