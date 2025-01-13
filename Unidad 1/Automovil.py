class Automovil():

    def __init__(self, modelo, color, altura) -> None:
        self.modelo = modelo
        self.color = color
        self.altura = altura
        self.esta_encendido = False
        print(f"Auto '{modelo}', color '{color}' y altura '{altura}' metros.")

    def encender(self):
        if self.esta_encendido:
            print("El auto ya está encendido.")
        else:
            print("Verificando si existe combustible...")
            print("Verificando controles...")
            print("El auto se ha encendido.")
            self.esta_encendido = True

    def acelerar(self):
        if self.esta_encendido:
            print("El auto está acelerando...")

    def frenar(self):
        if self.esta_encendido:
            print("El auto está frenando...")


auto1 = Automovil("Chevrolet", "Blanco", 1.95)
auto1.encender()
auto1.acelerar()

print("=====================================")

auto2 = Automovil("Kia", "Azul", 1.60)
auto2.encender()
auto2.frenar()

print("=====================================")
