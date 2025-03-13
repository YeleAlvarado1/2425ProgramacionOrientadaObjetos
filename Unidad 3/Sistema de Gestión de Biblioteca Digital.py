import json
import os

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def to_dict(self):
        #Convierte el objeto Libro en un diccionario para guardarlo en JSON.
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "isbn": self.isbn
        }

    @classmethod
    def from_dict(cls, data):
        #Convierte un diccionario de JSON en un objeto Libro.
        return cls(data['titulo'], data['autor'], data['categoria'], data['isbn'])

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.categoria} (ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def to_dict(self):
        #Convierte el objeto Usuario en un diccionario para guardarlo en JSON
        return {
            "nombre": self.nombre,
            "user_id": self.user_id,
            "libros_prestados": [libro.isbn for libro in self.libros_prestados]  # Guardamos solo los ISBN
        }

    @classmethod
    def from_dict(cls, data):
        #Convierte un diccionario de JSON en un objeto Usuario."""
        usuario = cls(data['nombre'], data['user_id'])
        # Aquí asignamos los libros prestados desde el archivo JSON
        return usuario

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros con ISBN como clave
        self.usuarios = {}  # Diccionario de usuarios con ID como clave
        self.cargar_datos()

    def cargar_datos(self):
        #Cargar datos desde el archivo JSON
        if os.path.exists("data.json"):
            with open("data.json", "r") as f:
                data = json.load(f)
                # Cargar libros
                for libro_data in data.get("libros", []):
                    libro = Libro.from_dict(libro_data)
                    self.libros[libro.isbn] = libro
                # Cargar usuarios
                for usuario_data in data.get("usuarios", []):
                    usuario = Usuario.from_dict(usuario_data)
                    self.usuarios[usuario.user_id] = usuario

    def guardar_datos(self):
        #Guardar datos a un archivo JSON
        data = {
            "libros": [libro.to_dict() for libro in self.libros.values()],
            "usuarios": [usuario.to_dict() for usuario in self.usuarios.values()]
        }
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        self.guardar_datos()  # Guardar después de añadir un libro

    def listar_libros(self):
        if self.libros:
            # Formato visual mejorado para la lista de libros
            print("=" * 80)
            print(f"{'ISBN':<15} {'Título':<25} {'Autor':<25} {'Categoría':<15}")
            print("=" * 80)
            for libro in self.libros.values():
                print(f"{libro.isbn:<15} {libro.titulo:<25} {libro.autor:<25} {libro.categoria:<15}")
            print("=" * 80)
        else:
            print("No hay libros en la biblioteca.")

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.user_id] = usuario
        self.guardar_datos()  # Guardar después de registrar un usuario

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            self.guardar_datos()  # Guardar después de dar de baja a un usuario

    def prestar_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print("Error: Usuario no registrado.")
            return

        if isbn not in self.libros:
            print("Error: Libro no disponible.")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[user_id]

        if libro in usuario.libros_prestados:
            print(f"El usuario {usuario.nombre} ya tiene el libro {libro.titulo} prestado.")
        else:
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
            self.guardar_datos()  # Guardar después de prestar un libro

    def devolver_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print("Error: Usuario no registrado.")
            return

        if isbn not in self.libros:
            print("Error: Libro no disponible.")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[user_id]

        if libro in usuario.libros_prestados:
            usuario.devolver_libro(libro)
            print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
            self.guardar_datos()  # Guardar después de devolver un libro
        else:
            print("Error: El libro no fue prestado por el usuario.")

    def buscar_libro(self, criterio, valor):
        resultados = []
        valor = valor.lower()  # Convertimos el valor de búsqueda a minúsculas

        if criterio == "titulo":
            resultados = [libro for libro in self.libros.values() if valor in libro.titulo.lower()]
        elif criterio == "autor":
            resultados = [libro for libro in self.libros.values() if valor in libro.autor.lower()]
        elif criterio == "categoria":
            resultados = [libro for libro in self.libros.values() if valor in libro.categoria.lower()]
        elif criterio == "isbn":
            if valor in self.libros:
                resultados.append(self.libros[valor])

        return resultados

    def listar_libros_prestados(self, user_id):
        if user_id not in self.usuarios:
            print("Usuario no registrado.")
            return []
        usuario = self.usuarios[user_id]
        return usuario.libros_prestados


# Función del menú interactivo
def menu():
    biblioteca = Biblioteca()

    while True:
        # Crear un cuadro visual alrededor del menú
        print("=" * 40)
        print("      LA BIBLIOTECA DIGITAL YS")
        print("=" * 40)
        print(f"1. Registrar Usuario")
        print("2. Dar Baja Usuario")
        print("3. Añadir Libro")
        print("4. Quitar Libro")
        print("5. Prestar Libro")
        print("6. Devolver Libro")
        print("7. Buscar Libro")
        print("8. Listar Libros Prestados")
        print("9. Listar Todos los Libros")
        print("10. Salir")
        print("=" * 40)

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del usuario: ")
            user_id = input("Introduce un ID único para el usuario (ejemplo: '001'): ")

            if user_id in biblioteca.usuarios:
                print(f"Error: El ID de usuario {user_id} ya está registrado.")
            else:
                usuario = Usuario(nombre, user_id)
                biblioteca.registrar_usuario(usuario)
                print(f"Usuario {nombre} registrado con éxito con ID: {user_id}.")

        elif opcion == "2":
            user_id = input("ID de usuario para dar de baja: ")
            biblioteca.dar_baja_usuario(user_id)
            print(f"Usuario con ID {user_id} dado de baja.")

        elif opcion == "3":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)
            print(f"Libro '{titulo}' añadido a la biblioteca.")

        elif opcion == "4":
            isbn = input("ISBN del libro a quitar: ")
            if isbn in biblioteca.libros:
                del biblioteca.libros[isbn]
                biblioteca.guardar_datos()  # Guardar después de quitar el libro
                print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
            else:
                print("El libro con ese ISBN no está en la biblioteca.")

        elif opcion == "5":
            user_id = input("ID de usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(user_id, isbn)

        elif opcion == "6":
            user_id = input("ID de usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(user_id, isbn)

        elif opcion == "7":
            criterio = input("Buscar por (titulo/autor/categoria/isbn): ").lower()
            valor = input(f"Introduce el {criterio}: ").lower()
            resultados = biblioteca.buscar_libro(criterio, valor)
            if resultados:
                for libro in resultados:
                    print(libro)
            else:
                print(f"No se encontraron libros por {criterio}: {valor}.")

        elif opcion == "8":
            user_id = input("ID de usuario: ")
            libros_prestados = biblioteca.listar_libros_prestados(user_id)
            if libros_prestados:
                for libro in libros_prestados:
                    print(libro)
            else:
                print(f"No hay libros prestados por el usuario con ID {user_id}.")

        elif opcion == "9":
            # Listar todos los libros de la biblioteca
            print("\nLibros en la biblioteca:")
            biblioteca.listar_libros()

        elif opcion == "10":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
