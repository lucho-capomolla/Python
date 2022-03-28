import string 
import random

caracteres = list(string.ascii_letters + string.digits + "!#@&%$()/\+")

def obtenerClave():
    longitud = int(input("Longitud de la clave: "))
    # Mezcla los caracteres
    random.shuffle(caracteres)
    clave = []
    for i in range(longitud):
        clave.append(random.choice(caracteres))
    random.shuffle(clave)
    return ("".join(clave))

if __name__ == "__main__":
    clave = obtenerClave()
    print(f"La clave seleccionada es: {clave}")