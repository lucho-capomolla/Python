from random import randint as azar
# 'azar' es un alias, para tener un nombre mas descriptivo y 
#       no escribir siempre 'randint', y saber para que lo queremos utilizar

# from random import *  // Obtiene todo desde la libreria, pero no es recomendable
continua = "s"
while(continua=="s" or continua=="S"):
    lanzaDado = azar(1,6)
    # lanzaDado = random.randint(1,6) // Otra alternativa
    print("Has sacado un " + str(lanzaDado))
    continua = input("Continuar(S/N)?")
print("Ya no se tira más el dado.")