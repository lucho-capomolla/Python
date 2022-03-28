import os

# Crear carpeta o directorio
os.makedirs("MiCarpeta")
# Listar el contenido
print(os.listdir("./"))
# Mostrar directorio actual
print(os.getcwd())
# Mostrar tamaño de la carpeta o directorio
print(os.path.getsize("MiCarpeta"))
# Comprobar si es archivo
print(os.path.isfile("MiCarpeta"))
# Comprobar si es carpeta
print(os.path.isdir("MiCarpeta"))
# Cambiar de directorio
os.chdir("MiCarpeta")
print(os.getcwd())
print(os.listdir("./"))
os.chdir("../")
print(os.getcwd())
# Renombrar carpeta
os.rename("MiCarpeta", "Mi_Carpeta")
# Borrar archivo
os.remove(os.getcwd() + "/archivo.txt")
print(os.listdir("./"))
# Borrar carpeta
os.rmdir("Mi_Carpeta")
os.chdir("../")
print(os.listdir("./"))