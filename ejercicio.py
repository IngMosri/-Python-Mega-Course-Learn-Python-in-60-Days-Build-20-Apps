#!/usr/bin/env python3

# Solicitar al usuario que ingrese el título del libro
text_title = input("Ingrese el título del libro:\n")

# Calcular la longitud del título
longitud = len(text_title)

# Imprimir la longitud del título
print(f"\nEl título ingresado tiene {longitud} caracteres.\n")

# Verificar si el título contiene más de 100 caracteres
if longitud > 100:
    print("El título ingresado contiene más de 100 caracteres.\n")

# Verificar si el título contiene solo caracteres alfabéticos
if text_title.replace(" ", "").isalpha():
    print("El título contiene caracteres válidos (solo letras).\n")
else:
    print("El título del libro contiene caracteres inválidos (no solo letras).\n")

# Imprimir el título del libro para confirmar la entrada
print(f"Título del libro ingresado: {text_title}")
