import random
import string

# Conjuntos de caracteres
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_chars = string.punctuation

# Solicitar la longitud de la contraseña
length = int(input("Enter the length of the password: "))

# Preguntar si se deben incluir diferentes tipos de caracteres
include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

# Crear una lista con los conjuntos de caracteres seleccionados
char_pool = ""
if include_lowercase:
    char_pool += lowercase
if include_uppercase:
    char_pool += uppercase
if include_digits:
    char_pool += digits
if include_special_chars:
    char_pool += special_chars

# Verificar que al menos un conjunto de caracteres fue seleccionado
if char_pool:
    password = ''.join(random.choice(char_pool) for _ in range(length))
    print("Generated password:", password)
else:
    print("You must select at least one character set!")
