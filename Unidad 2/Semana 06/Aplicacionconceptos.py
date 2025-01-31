# Clase base Personaje
class Personaje:
    def __init__(self, nombre, nivel, salud, especie, transformarse):
        self.nombre = nombre
        self.nivel = nivel  # Nivel de pelea del personaje
        self.__salud = salud #Encapsulamiento
        self.especie = especie
        self.__transformarse = transformarse  #Encapsulamiento

    # El nivel no supera el máximo
    def establecer_nivel(self, nivel):
        if nivel <= 500:
            self.nivel = nivel
        else:
            print(f"El nivel de pelea no puede superar 500. Nivel establecido a 500.")
            self.nivel = 500

    # Encapsulamiento para acceder a modificar valores
    def get_salud(self):
        return self.__salud

    def set_salud(self, nueva_salud):
        self.__salud = nueva_salud

    def get_transformarse(self):
        return self.__transformarse

    def set_transformarse(self, nuevo_transformarse):
        self.__transformarse = nuevo_transformarse

    # Polimorfismo
    def atacar(self):
        print(f"{self.nombre} está atacando.")

    # Pelea para saber el ganador
    def pelear(self, oponente):
        # Mostrar el enfrentamiento
        print(f"\n{self.nombre} vs {oponente.nombre}")

        # Realizar ataques primero
        self.atacar()
        oponente.atacar()

        # Usar habilidades específicas
        if isinstance(self, Vampiro):
            self.chupar_sangre()
        if isinstance(oponente, Licantropo):
            oponente.mordedura()

        # Determinar el ganador después de los ataques
        if self.nivel > oponente.nivel:
            print(f"{self.nombre} gana la pelea!")
        elif self.nivel < oponente.nivel:
            print(f"{oponente.nombre} gana la pelea!")
        else:
            print("Es un empate.")


# Clase Vampiro que hereda de Personaje (HERENCIA)
class Vampiro(Personaje):
    def __init__(self, nombre, nivel, salud, especie, transformarse, chupasangre=True):
        super().__init__(nombre, nivel, salud, especie, transformarse)
        self.chupasangre = chupasangre
        self.__nivel_chupar_sangre = 450  # Nivel de habilidad de chupar sangre

    # Acceder para modificar niveles
    def establecer_nivel_chupar_sangre(self, nivel):
        if nivel <= 500:
            self.__nivel_chupar_sangre = nivel
        else:
            print(f"El nivel de chupar sangre no puede superar 500. Nivel establecido a 500.")
            self.__nivel_chupar_sangre = 500

    def atacar(self):
        print(f"{self.nombre} ataca con sus colmillos vampiricos!")

    def chupar_sangre(self):
        print(f"{self.nombre} chupa sangre de su enemigo con un poder de nivel {self.__nivel_chupar_sangre}.")


# Clase Licantropo que hereda de Personaje
class Licantropo(Personaje):
    def __init__(self, nombre, nivel, salud, especie, transformarse, mordedura_mortal=True):
        super().__init__(nombre, nivel, salud, especie, transformarse)
        self.mordedura_mortal = mordedura_mortal
        self.__nivel_mordedura = 300  # Nivel de habilidad de mordedura mortal

    # Acceder a modificar al nivel de mordedura (encapsulamiento)
    def establecer_nivel_mordedura(self, nivel):
        if nivel <= 500:
            self.__nivel_mordedura = nivel
        else:
            print(f"El nivel de mordedura no puede superar 500. Nivel establecido a 500.")
            self.__nivel_mordedura = 500

    def atacar(self):
        print(f"{self.nombre} ataca con sus garras y colmillos de lobo!")

    def mordedura(self):
        print(f"{self.nombre} ha dado una mordedura mortal a su enemigo con un poder de nivel {self.__nivel_mordedura}.")


# Crear instancias de los personajes
lestad = Vampiro("Lestad", 300, 100, "Vampiro", True)
van_helsing = Licantropo("Van Helsing", 200, 120, "Licantropo", True)

# Mostrar la pelea
lestad.pelear(van_helsing)
