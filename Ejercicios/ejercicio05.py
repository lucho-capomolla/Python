# 05. El ordenador piensa un numero y el usuario tiene que adivinarlo, muestra tambien el numero de intentos.
from random import randint as azar


def pedirNumero():
    numero = int(input("Adivina el número que he pensado: "))
    return numero

def pensarNumero():
    piensaNumero = azar(1,100)
    return piensaNumero


def ejercicio05():
    piensaNumero = pensarNumero()
    numeroUsuario = pedirNumero()
    intentos = 0
    continua = True
    while continua:
        if numeroUsuario < piensaNumero:
            print("El número pensado es mayor...")
            intentos += 1
            numeroUsuario = pedirNumero()
        elif numeroUsuario > piensaNumero:
            print("El número pensado es menor...")
            intentos += 1
            numeroUsuario = pedirNumero()
        else:
            print("Adivinaste!!")
            print(f"Se ha adivinida en {intentos} intentos.")
            
            continuar = input("Quieres continuar? S/N: ")
            if(continuar=="S" or continuar=="s"):
                continua = True
                intentos = 0
                piensaNumero = pensarNumero()
                numeroUsuario = pedirNumero()
            else:
                continua = False
    print("Fin del juego.")
    
    
# Para ejecutar el programa
ejercicio05()