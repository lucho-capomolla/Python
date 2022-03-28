# Solicitar una lista al usuario, ordenarla e indicar con otras listas los numeros pares e impares.

def solicitarLista():
    lista = []
    num = None
    while num!= 0:
        num = int(input("Ingrese un número para agregarlo a la lista: (0 para terminar) "))
        if num>0:
            lista.append(num)
        elif num==0:
            break
        else:
            print("El número tiene que ser mayor a 0.")
    return lista

def ordenarLista(lista):
    lista.sort()

def separarXParidad(lista):
    pares = []
    impares = []
    for num in lista:
        if num%2==0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares
    
# Función principal  
def main():
    lista = solicitarLista()
    print(lista)
    ordenarLista(lista)
    print(f"Lista ordenada: {lista}")
    pares, impares = separarXParidad(lista)
    print(f"Los pares: {pares}")
    print(f"Los impares: {impares}")

# Ejecutando el código principal
main()