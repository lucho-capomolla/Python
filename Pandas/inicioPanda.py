# Pandas sirve para el análisis de datos
import pandas as pd
# Numpy sirve para realizar matrices o vectores
import numpy as np

etiquetas = ['a','b','c','d','e']
datos = np.arange(4,9)
serie = pd.Series(datos, index=etiquetas)
print(serie)
# Acceder valor de la serie
print(serie['c']) # Valor de la etiqueta 'c'
print("\n")

# Datos distintos tipo
datos = ['Pepe', 49, 'Mar', 46]
serie = pd.Series(datos) # Por omisión de index, 
# entonces la etiqueta toma como valor predeterminado desde el 0
print(serie)
print("\n")

# Datos directos
# Ya entiende que el 1er valor son los datos, y el segundo las etiquetas
serie = pd.Series([1000,500,1200,700], ['Emp01', 'Emp02', 'Emp03', 'Emp04'])
print(serie)
print("\n")

# Operación Suma
serie1 = pd.Series([1000,500,1200,700], ['Emp01', 'Emp02', 'Emp03', 'Emp04'])
print(serie1)
serie2 = pd.Series([1500,700,2200,900], ['Emp01', 'Emp02', 'Emp03', 'Emp04'])
print(serie2)
print("\n")
serie3 = serie1 + serie2
print(serie3)
print("\n")

# Dataframes
filas = ['Tienda1', 'Tienda2', 'Tienda3', 'Tienda4']
columnas = ['Articulo1', 'Articulo2', 'Articulo3']
datos = [[224,100,200], [np.nan,100,300], [300,np.nan,400], [400,100,500]]
dataframe = pd.DataFrame(datos, index=filas, columns=columnas)
print(dataframe)
print("\n")

# Seleccionar fila del Dataframe
print(dataframe.loc[['Tienda2', 'Tienda3']])
print("\n")
print(dataframe.iloc[1]) # Por índice
print("\n")

# Seleccionar columna del Dataframe
print(dataframe['Articulo3'])
print("\n")

# Valor concreto
print(dataframe.loc['Tienda2', 'Articulo3'])
print("\n")

# Nueva columna
dataframe['Articulo4'] = 25
print(dataframe)
print("\n")
dataframe['Total'] = dataframe['Articulo1'] + dataframe['Articulo2'] + dataframe['Articulo3'] + dataframe['Articulo4']
print(dataframe)
print("\n")

# Eliminar columna
#dataframe = dataframe.drop(['Total'], axis=1)
print(dataframe.drop(['Total'], axis=1, inplace=True)) # inplace: para que cause efecto 
print(dataframe)
print("\n")

condicion = dataframe > 200
print(dataframe[condicion]) # Solo muestra los que cumplen la condición
condicion2 = (dataframe['Articulo1'] >= 200) | (dataframe['Articulo2'] >= 200)
print(dataframe[condicion2]) # Solo muestra los que cumplen la condición
print("\n")

nuevaColumna = '1 2 3 4'.split()
dataframe['Indices'] = nuevaColumna
print(dataframe)
dataframe = dataframe.set_index('Indices')
print(dataframe)
print("\n")

# Sustituir los valores nulos con otros
dataframe.fillna(value=0, inplace=True)
print(dataframe)
print("\n")

# Elimina todas las columnas que tenga valores nulos (Na)
#dataframe.dropna(axis=1, inplace=True)
#print(dataframe)

# Unión de Dataframes
data1 = dataframe.copy()
data2 = dataframe.copy()
print(data1)
print(data2)
# Axis = 1, se unen por columna
# Axis = 0, se unen por fila
dataTotal = pd.concat([data1, data2], axis=0)
print(dataTotal)
print("\n")
# Valores únicos 
print(dataTotal['Articulo2'].unique())
# Cantidad de veces repetido
print(dataTotal['Articulo2'].value_counts())
print("\n")

# Mostrar columnas
print(dataTotal.columns)
# Mostrar índices
print(dataTotal.index)
# Ordenar valores según ...
print(dataTotal.sort_values(['Articulo3']))
# Descripciones con estadísticas
print(dataTotal.describe())
print("\n")

# Pasar Dataframe a un fichero CSV
dataTotal.to_csv('datatotal.csv')
print("\n")

# Obtener de un fichero CSV para pasarlo a un Dataframe
dataframe = pd.read_csv('dataTotal.csv', index_col=0)
print(dataframe)