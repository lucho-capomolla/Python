# 9. Crea una variable numerica, si esta entre 0 y 20 mostrar un mensaje.

def ejercicio09():
    variableNumerica = int(input("Ingrese un número: "))
    if (variableNumerica >= 0 and variableNumerica <= 20):
        print("El número está entre 0 y 20.")
    else:
        print("El número no está entre 0 y 20.")
        
# Para ejecutar el programa
ejercicio09()