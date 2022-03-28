# 04. Mostrar los numeros pares en un intervalo dado como del 1 al 50 y contar cuantos son.

def esPar(num):
    if num%2 == 0:
        return True
    else:
        return False

def ejercicio04():
    cantidadPares = 0
    for numero in range(1,51):
        if esPar(numero):
            print(numero)
            cantidadPares += 1
    print(f"Cantidad total de pares: {cantidadPares}")
    

# Para ejecutar el programa 
ejercicio04()