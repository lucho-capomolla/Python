# 13. Generar un rango desde 0 hasta la longitud de una cadena dada.

def ejercicio14():
    cadena = input("Ingrese una cadena: ")
    longitudCadena = len(cadena)
    
    rango = list(range(longitudCadena+1))
    print(rango)
    
ejercicio14()