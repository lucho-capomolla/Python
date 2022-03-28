# 07. Sumar los numeros pares y por otro los impares dentro del intervalo del 1 al 50.

def esPar(num):
    if(num%2 == 0):
        return True
    else:
        return False
    
def ejercicio07():
    cantidadPares = 0
    sumaPares = 0
    cantidadImpares = 0
    sumaImpares = 0
    
    for numero in range(1,51):
        if esPar(numero):
            sumaPares += numero
            cantidadPares += 1
        else:
            sumaImpares += numero
            cantidadImpares += 1
    
    print(f"\nSuma total de los pares: {sumaPares}")
    print(f"Cantidad total de pares: {cantidadPares}")
    print(f"Suma total de impares: {sumaImpares}")
    print(f"Cantidad total de impares: {cantidadImpares}")
    
# Ejecuto programa
ejercicio07()