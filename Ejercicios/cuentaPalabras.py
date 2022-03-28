# Cuenta la cantidad de veces que se encuentra una palabra en un texto dado

### Función CuentaPalabras
def cuentaPalabras(texto):
    palabras = texto.split(" ")
    palabrasContadas = {}
    contador = 0
    longitud = len(palabras)
    
    for i in range(0, longitud):
        primera = palabras[i]
        for j in range(0, longitud):
            segunda = palabras[j]
            if primera == segunda:
                contador += 1
        palabrasContadas[primera] = contador
        contador = 0
    return palabrasContadas

# Ejemplo
#print(cuentaPalabras("Hola mundo como anda todo el mundo mundo mundo ?"))
# > {'Hola': 1, 'mundo': 4, 'como': 1, 'anda': 1, 'todo': 1, 'el': 1, '?': 1}


### Contando palabras desde un archivo
try:
    fichero = open("ejemploCuentaPalabras.txt", "r", encoding="utf-8")
    texto = fichero.read()
    print(cuentaPalabras(texto))
except:
    print("No se ha podido leer el fichero.")
finally:
    fichero.close()


### Contar las palabras de un texto escrito por consola
texto = input("Escribir un texto para contar las palabras repetidas: ")
print(cuentaPalabras(texto))
    
    
