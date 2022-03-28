# 02. Crea una calculadora basica, incluyendo menu opciones y comprobando que no se intente dividir por cero.

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
    try:
        resultado = num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        resultado = 0
    return resultado


# Estructura de la Calculadora
def menu():
    print("1) Suma")
    print("2) Resta")
    print("3) Producto")
    print("4) División")
    opcion = int(input("> "))
    return opcion


def solicitarDatos():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    return num1, num2


def operacion(operacion):
    num1, num2 = solicitarDatos()
    if operacion == 1:
        resultado = suma(num1, num2)
    elif operacion == 2:
        resultado = resta(num1, num2)
    elif operacion == 3:
        resultado = producto(num1, num2)
    elif operacion == 4:
        resultado = division(num1, num2)
    return resultado


def ejercicio02():
    continuar = True
    while continuar:
        opcion = menu()
        
        # Verifica que la opción se encuentre en el rango disponible (1,2,3,4)
        if(opcion <= 4 and opcion >= 1):
            resultado = operacion(opcion)
            print(f"Resultado de la operación: {resultado}")
            
            # Verificar si se desea terminar con la calculadora o se desea seguir haciendo cálculos
            opcionContinuar = input("¿Desea continuar? S/N: ") 
            if (opcionContinuar == "S" or opcionContinuar == "s"):
                continuar = True
            elif (opcionContinuar == "N" or opcionContinuar == "n"):
                continuar= False
            else:
                print("Ingrese una opción válida.")
        else:
            print("Ingrese una opción válida.")
        print("\n")
    print("Saliendo...")


# Para ejecutar la calculadora
ejercicio02()