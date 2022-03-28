# 16. Definir una funcion que calcule la suma y multiplicacion de una lista.
from typing import List

def ejercicio16():
    sumaTotal = 0
    productoTotal = 1
    
    lista = [1,2,3,4,5,6,7]
    
    for elemento in lista:
        sumaTotal += elemento
        productoTotal *= elemento
        
    print(f"La suma total de la lista es {sumaTotal}")
    print(f"El producto total de la lista es {productoTotal}")

ejercicio16()