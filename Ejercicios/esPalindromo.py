
def esPalindromo(cadena):
    cadenaInversa = cadena[::-1]
    if cadena == cadenaInversa:
        return True
    else:
        return False

# Usando un If ternario
def esPalindromoCorto(cadena):
    return True if cadena == cadena[::-1] else False


cadena = "neuquen"
print(esPalindromo(cadena))
print(esPalindromoCorto(cadena))