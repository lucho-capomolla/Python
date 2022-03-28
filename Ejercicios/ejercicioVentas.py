import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("datos.csv")
print("Inicio del Dataframe")
print(datos.head(5))
print("Final del Dataframe")
print(datos.tail(5))
print("\n")

# Información con los Tipos de datos 
print(datos.info())
print("\n")

# Estadísticas del Dataframe
print(datos.describe())
print("\n")

# Columnas
print(datos.columns)
# Índices
print(datos.index)
print("\n")

datosAgrupados = datos.groupby('TIENDA').TOTAL.sum()
print(datosAgrupados.head(5))

plt.pie(datosAgrupados, labels=datosAgrupados.index)
plt.show()