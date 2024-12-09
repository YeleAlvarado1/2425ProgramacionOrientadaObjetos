# Clase abstracción (la base)
class Animal:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def hacer_sonido(self):
        pass

# Clase derivada
class AnimalDeGranja(Animal):
    def __init__(self, nombre, raza, tipo_alimento):
        # Llama al constructor de Animal
        super().__init__(nombre, raza)
        self.tipo_alimento = tipo_alimento

    def alimentar(self):
        print(f"Alimentando a {self.nombre} con {self.tipo_alimento}.")

# Clase Vaca (hereda de AnimalDeGranja)
class Vaca(AnimalDeGranja):
    def __init__(self, nombre, raza):
        # Llamamos al constructor de AnimalDeGranja
        super().__init__(nombre, raza, "pasto")

    def hacer_sonido(self):
        print(f"{self.nombre} la {self.raza} dice: ¡Muu!")

# Clase Mono (hereda de Animal)
class Mono(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} el {self.raza} dice: ¡Uhh uhh ahh ahh!")

# Crear objetos con nombre y raza
vaca = Vaca("Lola", "Vaca Holstein")
mono = Mono("Max", "Macaco")

# Llamamos al metodo hacer_sonido()
vaca.hacer_sonido()  # Salida: Lola la Vaca Holstein dice: ¡Muu!
mono.hacer_sonido()  # Salida: Max el Macaco dice: ¡Uhh uhh ahh ahh!

# Llamamos al metodo alimentar() para la Vaca
vaca.alimentar()  # Salida: Alimentando a Lola con pasto.