# Este programa permite al usuario calcular el área de tres figuras geométricas: Cuadrado, Rectángulo y Círculo.
# Ofrece un menú de opciones, utiliza diferentes tipos de datos y sigue la convención de nombres en snake_case.

def calcular_area_cuadrado(lado):       # Calcula el área de un cuadrado dado el valor de un lado.
    return lado ** 2

def calcular_area_rectangulo(base, altura):     # Calcula el área de un rectángulo dados la base y la altura.
    return base * altura

def calcular_area_circulo(radio):       # Calcula el área de un círculo dado el radio.
    pi = 3.14159  # valor de pi necesario para obtener el área de un círculo.
    return pi * (radio ** 2)

def mostrar_menu():     # Muestra el menú de opciones al usuario.
    print("\nMenú de Opciones:")
    print("1. Calcular área de un cuadrado")
    print("2. Calcular área de un rectángulo")
    print("3. Calcular área de un círculo")
    print("4. Salir")

# Variable booleana para controlar el ciclo del menú.
continuar_programa = True

while continuar_programa:   # Mientras sea TRUE el programa continua ejecutándose
    mostrar_menu()  # Muestra las opciones al usuario.
    opcion_seleccionada = input("Seleccione una opción (1-4): ")  # Almacena la opción seleccionada como cadena de texto en una variable tipo string.

    if opcion_seleccionada == "1":
        # Calcula el área del cuadrado
        lado = float(input("Ingrese el valor del lado del cuadrado: "))
        area_cuadrado = calcular_area_cuadrado(lado)
        print(f"El área del cuadrado es: {area_cuadrado:.2f}")

    elif opcion_seleccionada == "2":
        # Calcula el área del rectángulo
        base = float(input("Ingrese el valor de la base del rectángulo: "))
        altura = float(input("Ingrese el valor de la altura del rectángulo: "))
        area_rectangulo = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area_rectangulo:.2f}")

    elif opcion_seleccionada == "3":
        # Calcula el área del círculo
        radio = float(input("Ingrese el valor del radio del círculo: "))
        area_circulo = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area_circulo:.2f}")

    elif opcion_seleccionada == "4":
        # Salir del programa
        print("Gracias por usar el programa")
        continuar_programa = False  # Cambiamos la variable booleana para salir del bucle.

    else:
        # Opcion inválida si en el Menú de Opciones se ingresa un valor diferente a los solicitados
        print("Opción inválida. Por favor, seleccione una opción del menú.")
