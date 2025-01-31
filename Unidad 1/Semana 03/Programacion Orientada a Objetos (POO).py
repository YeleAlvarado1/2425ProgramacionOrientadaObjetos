#clase (base)vgestiona temperaturas diarias
class ClimaDiario:
    def __init__(self):
        # Lista para almacenar las temperaturas diarias
        self.temperaturas = []

    def ingresar_temperatura(self, dia):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        self.temperaturas.append(temp)

    #Metodo para calcular el promedio de las temperaturas
    def calcular_promedio(self):
        if len(self.temperaturas) == 0:
            # Evitar división por cero
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

# Clase principal que gestiona temperatura de la semana de clima
class ClimaSemanal:
    def __init__(self):
        #  un clima semanal tiene un clima diario
        self.clima_diario = ClimaDiario()

    def ingresar_temperaturas(self):
        # Dias de la semana 1 a 7
       for dia in range(1, 8):
            self.clima_diario.ingresar_temperatura(dia)

    def mostrar_promedio(self):
        promedio = self.clima_diario.calcular_promedio()
        print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

# Ejecutar el programa
if __name__ == "__main__":
    print("Promedio Semanal del Clima")
    # Crear objeto de la clase ClimaSemanal
    clima_semanal = ClimaSemanal()
    # Ingresar temperaturas
    clima_semanal.ingresar_temperaturas()
    # Mostrar el promedio calculado
    clima_semanal.mostrar_promedio()
