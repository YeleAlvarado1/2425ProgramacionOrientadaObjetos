# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    # Se ingresan 7 días
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio de las temperaturas
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal llama a las funciones segun sea necesario
def main():
    print("Promedio Semanal del Clima")
    # Llama a la función para ingresar datos
    temperaturas = ingresar_temperaturas()
    # Calcula el promedio
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

# Ejecutar el programa
if __name__ == "__main__":
    main()
