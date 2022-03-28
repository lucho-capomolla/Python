# Contar la cantidad de vocales que tiene un texto

def esVocal(letra):
    vocales = "AEIOUaeiou"

    if letra in vocales:
        return True
    else:
        return False 
    
def cuentaVocales():
    texto = input("Ingrese un texto: ")
    cantidadVocales = 0
    for letra in texto:
        if esVocal(letra):
            cantidadVocales += 1
    print(f"En total hay {cantidadVocales} vocales en el texto.")
    
cuentaVocales()