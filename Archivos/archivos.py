# Guardar datos en un archivo
# - Abrir archivo
escritura = open("archivo.txt", "w")
escritura.write("Esto se escribe en el archivo \n esto esta en la linea inferior") 
escritura.close()

# - Lectura de archivo
lectura = open("archivo.txt", "r")
#   - Leer una línea
leeLinea = lectura.readline()
# readlines: lee todo pero linea a linea, lo toma como una 'Lista'
print("Leyendo una línea: " + leeLinea)
lectura.close()
#   - Leer todo el fichero
lectura = open("archivo.txt", "r")
leeTodo = lectura.read()
print("Leyendo todo el archivo: \n" + leeTodo)
lectura.close()