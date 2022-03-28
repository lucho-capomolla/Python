# 18. Definir funcion que indique si el caracter pasado es vocal o no.

def esVocal(letra):
    if(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
        return True
    else:
        return False
    
def ejercicio18():
    letra = input("Ingrese una letra: ")
    letra = letra.lower()
    
    if esVocal(letra):
        print("Es Vocal.")
    else:
        print("No es Vocal.")


ejercicio18()