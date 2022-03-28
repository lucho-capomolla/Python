import time


def cuentaAtras():
    for contador in range(10,-1,-1):
        if contador != 0:
            print(f"\r{contador}", end=" ")
            time.sleep(1)
        else:
            print(f"\r{contador}", end=" ")
            print("\nFin de la cuenta atrás")
            
cuentaAtras()