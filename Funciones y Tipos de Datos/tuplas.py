colores = ("verde", "amarillo", "rojo", "azul")
# También puede crearse sin los paréntesis
print(type(colores))
print(colores)

# Tupla Vacía
tupla_vacia = ()

# A diferencia de las listas, las tuplas no se pueden modificar
#colores[2] = "rosa"       // No se pueden modificar valores dentro de la tupla

# Len: obtener el tamaño de una tupla
print(len(colores))

# Tupla unitaria
tuplaUnitaria = (50,)
print(type(tuplaUnitaria))
print(tuplaUnitaria)

# Empaquetado de tuplas
a = 10
b = "Pepe"
c = 22.34
tupla = a,b,c
print(type(tupla))
print(tupla)

# Desempaquetado de tuplas
# Tener en cuenta del tamaño de la tupla para poder asignarle las variables
a,b,c = tupla
print(a)
print(b)
print(c)