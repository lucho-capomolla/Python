# 01. Crea una funcion que indique que numero de los pasados por parametros es mayor o si son iguales.

# Otra forma:
def mayor(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return False
    
    
def ejercicio01():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo número: "))
    
    numMayor = mayor(numero1, numero2)
    
    if numMayor:
        print(f"El número {numMayor} es el mayor de los dos.")
    else:
        print("Ambos números son iguales")
        
# Para pedir constantemente los números 
while 1:
    ejercicio01()
    
    
