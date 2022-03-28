# Una empresa tiene 3 productos de distinto peso que manda a los clientes a traves de otra empresa de mensajeria, 
# necesita un script que le indique que peso envia a cada cliente para indicarlo a la mensajeria.
# Se debe solicitar al usuario la cantidad a enviar de cada producto, conociendo que el peso es el siguiente:
    #Producto 1 pesa 1.5 kg
    #Producto 2 pesa 1.7 kg
    #Producto 3 pesa 2.1 kg

def envios():
    PESO01 = 1.5
    PESO02 = 1.7
    PESO03 = 2.1

    cantidad01 = int(input("Ingrese la cantidad del primer producto: "))
    cantidad02 = int(input("Ingrese la cantidad del segundo producto: "))
    cantidad03 = int(input("Ingrese la cantidad del tercer producto: "))

    pesoEnvio01 = PESO01 * cantidad01
    pesoEnvio02 = PESO02 * cantidad02
    pesoEnvio03 = PESO03 * cantidad03
    pesoTotal = pesoEnvio01 + pesoEnvio02 + pesoEnvio03

    print(f"El peso total del Envío 1 es de {round(pesoEnvio01, 2)} Kg")
    print(f"El peso total del Envío 2 es de {round(pesoEnvio02, 2)} Kg")
    print(f"El peso total del Envío 3 es de {round(pesoEnvio03, 2)} Kg")
    print(f"El peso total de todos los envíos es de {round(pesoTotal, 2)} Kg")
    
envios()