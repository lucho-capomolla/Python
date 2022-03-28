# 06. Muestra, suma y cuenta los numeros que son multiplos de 2 y 3 a la vez, que esten entre 1 y el valor que de el usuario.


def esMultiploDe(num, multiplo):
    if(num%multiplo == 0):
        return True
    else:
        return False


def ejercicio06():
    rangoMaximo = int(input("Ingrese el rango máximo: "))
    sumaTotal = 0
    cantidadNumeros = 0
    for numero in range(1, rangoMaximo+1):
        if(esMultiploDe(numero, 3) and esMultiploDe(numero, 2)):
            print(numero)
            sumaTotal += numero
            cantidadNumeros += 1

    print("La suma total de los números múltiplos es de " + str(sumaTotal))
    print("La cantidad total de múltiplos de 2 y de 3 es " + str(cantidadNumeros))
    
# Para ejecutar el programa
ejercicio06()