# Libreria de Python para operar con archivos
import os

# Operar con archivos
carpeta = "D:\Data User\Desktop\Cursos\Curso Python\Scripts\Archivos"
listado = os.listdir(carpeta)
print(listado)
print(type(listado))

# Filtrado
for archivo in listado:
    if archivo.endswith(".mp3"):
        print("Fichero MP3 encontrado.")
        print(f"Nombre fichero: {archivo}")

# Otra forma de filtrar
filtrado = [archivo for archivo in listado if archivo.endswith(".txt")]
print(type(filtrado))
print(filtrado)

# Cambio de directorio
  #os.chdir("directorio")
# Renombrar
  #os.rename("Viejo nombre", "Nuevo nombre")
# Borrar
  #os.chdir("Directorio")
  #os.remove("nombre Archivo")
  
# Renombrar varios archivos a la vez
contador = 1
for archivo in os.listdir():
    nombre, extension = os.path.splitext(archivo)
    print(nombre, extension)
    #nuevoNombre = f'{str(contador)}_{nombre}{extension}'
    contador+=1
    #os.rename(archivo, nuevoNombre)
    
# Copiar contenido de un fichero a otro
fichero = open("test.txt", "r")
nuevoFichero = open("nuevoText.txt", "r")
for linea in fichero:
    nuevoFichero.write(linea)
fichero.close()
nuevoFichero.close()

# En el caso que algún fichero no exista, se procede a:
try: 
    fichero = open("test.txt", "r")
    nuevoFichero = open("nuevoText.txt", "r")
    os.chdir("directorio")
    for linea in fichero:
        nuevoFichero.write(linea)
    fichero.close()
    nuevoFichero.close()
except FileNotFoundError:
    print("No se ha encontrado el fichero.")
    
# Otra forma con 'with'
# + La ventaja es que no hace falta hacer el archivo.close
try:
    with open("test.txt") as fichero:
        with open("nuevoFichero.txt", "w") as nuevoFichero:
            for linea in fichero:
                nuevoFichero.write(linea)
except FileNotFoundError:
    print("Fichero no encontrado.")