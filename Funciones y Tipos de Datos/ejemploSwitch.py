# Ejemplo: Se obtiene el numero del mes, y se lo pasa en letra

# En Python no existe la sentencia del Switch como este caso
#switch(num):
#    case 1:
#        break
#    case 2:
#        break

# Se utiliza mediante el uso de Diccionarios:
def dameMes(num):
    meses = {
        1 : "Enero", 
        2 : "Febrero",
        3 : "Marzo",
        4 : "Abril",
        5 : "Mayo",
        6 : "Junio",
        7 : "Julio",
        8 : "Agosto",
        9 : "Septiembre",
        10 : "Octubre",
        11 : "Noviembre",
        12 : "Diciembre"
    }  
    return meses.get(num, "Mes no válido")

mes = int(input("Introducir un número del 1 al 12 para saber el mes: "))
print(dameMes(mes))