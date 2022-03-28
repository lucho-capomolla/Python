import numpy as np

# Convertir una lista en una matriz o array
lista1 = [1,2,3,4,5,6,7,8,9]
array1 = np.array(lista1)
print(type(lista1))
print(lista1)
print(type(array1))
print(array1)

lista2 = [[1,2,4], [2,5,3], [9,4,2]]
array2 = np.array(lista2)
print(lista2)
print(array2)


# Arrays: Generación automática
arrayRango = np.arange(2,25,3)
print(arrayRango)
print("\n")
#   zeros((filas, columnas))
matrizCeros = np.zeros((4,5))
print(matrizCeros)
print("\n")
#   ones((filas, columnas))
matrizUnos = np.ones((4,5))
print(matrizUnos)
print("\n")

# Matriz de 40 elementos con valores del 2 al 6
matriz40 = np.linspace(2,6,40)
print(matriz40)
print("\n")

# Matriz identidad
matrizIdentidad = np.eye(7)
print(matrizIdentidad)
print("\n")

# Matriz con números aleatorios (valores entre 0 y 1)
matrizAleatoria = np.random.rand(3,4)
print(matrizAleatoria)
print("\n")
matrizAleatoriaNormal = np.random.randn(4)
print(matrizAleatoriaNormal)
print("\n")
# np.random.randint(desde, hasta, cantidadElementos) 
# cantidadElementos: 1 valor = cantidad total en una sola fila
# (fila, columna) para tomarlo como una matriz
matrizAleatoriaEnteros = np.random.randint(1,51,(4,4))
print(matrizAleatoriaEnteros)
print("\n")

# Pasar de un Array (o vector de 1 dimensión) a una Matriz de 5 filas x 6 columnas
arrayTam = np.random.randint(1,201,30)
print(arrayTam)
print("\n")
# Pasa el array a una matriz
matriz = arrayTam.reshape(5,6)
print(matriz)
print("\n")

# Max y min
array = np.random.randint(1,901,200)
print(array)
maximo = array.max()
print(f"El valor máximo es {maximo}")
# Se obtiene la ubicación del valor máximo
print(array.argmax())
minimo = array.min()
print(f"El valor mínimo es {minimo}")
# Se obtiene la ubicación del valor mínimo
print(array.argmin())

# Mostrar elementos de un Array (en una posición particular)
array = np.arange(1,11)
print(array)
print(array[2])
# De la posicion 5 en adelante
print(array[5:])
# Desde el inicio hasta la posición 6
print(array[:6])
print("\n")

# Copiar Array
array2 = array.copy()
print("\n")

# Mostrar elementos de una matriz
print(matriz)
print(matriz[0]) # Primer fila
print(matriz[:2]) # Desde el inicio hasta la tercer fila
print(matriz[1][2]) # Posición en particular
# print(matriz[1,2]) // Es lo mismo que arriba
print(matriz[:, 1]) # Toma todos los valores de una fila, de la columna 2
print(matriz[:, :1]) # Toma todos los valores de una fila, hasta la columna 2
print(np.max(matriz)) # Valor máximo de la Matriz
print("\n")
condicion = matriz > 100
print(matriz)
print(condicion)
print("\n")

# Numeros impares
condicion = (matriz % 2 != 0)
print(matriz[condicion])
print("\n")

# Ejercicio (pasando una lista a matriz)
lista = np.arange(5,41)
print("Mostrando una lista en dimensión 1:")
print(lista)
print("Mostrando una lista en una matriz de 3 x 12:")
lista = lista.reshape(3,12)
print(lista)
print("Mostrando valor en la posición 2 y 4:")
print(lista[2][4])
print("\n")

# Combinación primitiva (valores al azar)
arrayPrimitiva = np.random.randint(1,50,6)
print(f"La combinación ganadora de la primitiva será {arrayPrimitiva}")
