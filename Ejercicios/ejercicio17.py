# 17. Definir funcion que muestre una cadena al reves.

from audioop import reverse


def ejercicio17():
    cadena = input("Ingrese una cadena: ")
    cadenaInversa = cadena[::-1]
    
    print(f"Cadena: {cadena}\nCadena Inversa: {cadenaInversa}")
    
ejercicio17()