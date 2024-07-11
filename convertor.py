#!/usr/bin/env python3
print("Hola ingresa que es lo que quieres convertir: ")

def miles_km():
    print("Has seleccionado la conversión de Millas a Kilómetros")
    input_miles = input("Ingrese la cantidad de millas que desea convertir:\n")
    
    # Convertir la entrada a un número entero
    try:
        miles = float(input_miles)
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
    
    # Conversión de millas a kilómetros
    km = miles * 1.60934
    print(f"{miles} millas son {km} kilómetros.")

def km_to_miles():
    print("Has seleccionado Kilómetros a Millas.")
    input_km = input("Ingrese la cantidad de kilómetros que desea convertir:\n")

    # Convertir la entrada a un número de punto flotante
    try:
        km = float(input_km)
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
    
    # Conversión de kilómetros a millas
    miles = km * 0.621371
    print(f"{km} kilómetros son {miles} millas.")



def fah_celcius():
    print("Has seleccionado fahrenheit a Celcius .")
    input_fah = input("Ingrese la cantidad a fahrenheit que desa convertir:\n")

    # conversion de Fahrenheit a Celcius
    try:
        fah = float(input_fah)
    except ValueError:
        print("Por favor ingrese un numero valido")
        return
    celcius = (fah - 32) * 5/9
    print(f"{fah} fahrenheit son {celcius} Celcius .")


def celsius_to_fahrenheit():
    print("Has seleccionado Celsius a Fahrenheit.")

    input_cel = input("Ingrese la cantidad de Celsius que desea convertir:\n")

    # Conversión de Celsius a Fahrenheit
    try:
        cel = float(input_cel)
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
    
    fahrenheit = cel * 9/5 + 32
    print(f"{cel} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.")


def salir():
    print("Saliendo del programa.")

def mostrar_menu():
    print("\nMenu de Opciones")
    print("1. Millas a kilometros")
    print("2. Kilometros a millas")
    print("3. fahrenheit a Celcius")
    print("4. celcius a fahrenheit")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-4): ")
    
    if opcion == '1':
        miles_km()
    elif opcion == '2':
        km_to_miles()
    elif opcion == '3':
        fah_celcius()
    elif opcion == '4':
        celsius_to_fahrenheit()
    elif opcion == '5':
        salir()

        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
