# 15. Definir una funcion que calcule la longitud de una cadena dada.

def ejercicio15():
    cadena = input("Ingrese una cadena: ")
    contador = 0
    for elemento in cadena:
        contador += 1
    print(f"La longitud de la cadena es de: {contador}")
    
ejercicio15()