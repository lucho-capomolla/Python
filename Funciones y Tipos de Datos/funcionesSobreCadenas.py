cadena = "EjEmplO dE CaDENa de tExtoS"
# Operaciones sobre las Cadenas de Textos
# - Pasar a minúsculas
print(cadena.lower())

# - Pasar a mayúsculas
print(cadena.upper())

# - Dejar solo letra Capital
print(cadena.capitalize())

# - Pasar a Mayúscula la primer letra de cada palabra
print(cadena.title())

# - Invertir mayúsculas a minúsculas, y viceversa
print(cadena.swapcase())

# Consultas sobre las cadenas de texto
# - Está en mayúsculas?
print(cadena.isupper())
cadena2 = "MAYUSCULAS"
print(cadena2.isupper())

# - Está en minúsculas?
print(cadena.islower())
cadena3 = "minusculas"
print(cadena3.islower())

# - Cadena es numérica?
print(cadena.isnumeric())

# - Cadena es alfanumérica?
print(cadena.isalnum())

# - Es un Título?
print(cadena.istitle())

# - Ajusta el texto en el centro
print(cadena.center(50, ' '))

# - Ajusta el texto a la izquierda
print(cadena.ljust(50, ' '))

# - Ajusta el texto a la derecha
print(cadena.rjust(50, ' '))

# - Quitar espacios vacíos
texto = "               Hola"
print(texto)
print(texto.strip())

# - Reemplazar caracter
print(cadena.replace("dE", "de"))

