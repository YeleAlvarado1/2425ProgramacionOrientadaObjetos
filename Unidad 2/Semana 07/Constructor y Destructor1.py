#Crear la clase
class Persona:
    def __init__(self, nombre, edad):   #Definir constructor
        self.nombre = nombre
        self.edad = edad
        print("¡Hola! Soy", self.nombre)

    def __del__(self):      #Definir destructor
        print(self.nombre, "se está despidiendo.")

# Creando objetos
persona1 = Persona("Juan", 30)
persona2 = Persona("Ana", 25)

# Los destructores se llaman cuando las referencias se pierden
del persona1
del persona2