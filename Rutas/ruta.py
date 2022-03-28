# Abrir ficheros o carpetas indicando una ruta

import os
import pandas as pd # Lectura de archivos CSV

# Directorio Actual
directorio_actual = os.getcwd()
print(directorio_actual)

# Directorio Datos
directorio_datos = os.path.join(directorio_actual, 'Rutas\datos')
print(directorio_datos)
print("Existe el directorio:")
print(os.path.exists(directorio_datos))
print("Es una carpeta o directorio?")
print(os.path.isdir(directorio_datos))

# Listar archivos de datos
listado = [os.path.join(directorio_datos, item) 
           for item in os.listdir(directorio_datos)]
print(listado)
print(os.listdir(directorio_datos))

# Crear carpeta nueva
try:
    carpeta_nueva = os.mkdir(os.path.join(directorio_actual, "Rutas\carpeta_nueva"))
    print(carpeta_nueva)
except FileExistsError:
    print("La carpeta ya existe.")

# Abrir fichero fuera de la carpeta 'datos'
fichero_exterior = os.path.join(directorio_actual, "Rutas\datos.csv")
df_exterior = pd.read_csv(fichero_exterior)
print("Mostrando fichero exterior")
print(df_exterior)

# Abrir fichero dentro de la carpeta 'datos'
fichero_interior = os.path.join(directorio_datos, "datos.csv")
df_interior = pd.read_csv(fichero_interior)
print("Mostrando fichero interior")
print(df_interior)

# Abriendo sin indicar ruta
fichero = "datos.csv"
df = pd.read_csv(fichero)
print("Fichero sin indicar ruta")
print(df)