
# Funciones Calculadora
# - Suma
def suma(num1, num2):
    resultado = num1 + num2
    return resultado

# - Resta
def resta(num1, num2):
    resultado = num1 - num2
    return resultado

# - Producto
def producto(num1, num2):
    resultado = num1 * num2
    return resultado

# - División
def division(num1, num2):
    resultado = num1 / num2
    return resultado

#Estructura de la Calculadora
def menu():
    print("1) Suma")
    print("2) Resta")
    print("3) Producto")
    print("4) División")
    print("5) Salir")
    opcion = int(input("- "))
    return opcion

def solicitarDatos():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    return num1, num2

def operacion(operacion, num1, num2):
    if operacion == "suma":
        resultado = suma(num1, num2)
    elif operacion == "resta":
        resultado = resta(num1, num2)
    elif operacion == "producto":
        resultado = producto(num1, num2)
    elif operacion == "division":
        resultado = division(num1, num2)
    return resultado

# Bucle para iniciar la Calculadora
while True:
    opcion = menu()
    if opcion == 1:
        num1, num2 = solicitarDatos()
        resultado = operacion("suma", num1, num2)
        print(f"El resultado de la suma entre {num1} y {num2} es = {resultado}\n")
    elif opcion == 2:
        num1, num2 = solicitarDatos()
        resultado = operacion("resta", num1, num2)
        print(f"El resultado de la resta entre {num1} y {num2} es = {resultado}\n")
    elif opcion == 3:
        num1, num2 = solicitarDatos()
        resultado = operacion("producto", num1, num2)
        print(f"El resultado del producto entre {num1} y {num2} es = {resultado}\n")
    elif opcion == 4:
        num1, num2 = solicitarDatos()
        if num2 == 0:
            print("El segundo número no puede ser 0.")
        else:
            resultado = operacion("division", num1, num2)
            print(f"El resultado de la division entre {num1} y {num2} es = {resultado}\n")
    elif opcion == 5:
        break
    else:
        print("Ingrese una opción válida.")
    print("\n")    
print("Saliendo...")