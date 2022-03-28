# Obtener el radio y longitud de un círculo
# Área: pi*r^2
# Longitud = 2*pi*r

import math

def obtenerRadioYLongitud():
    radio = float(input("Ingrese el Radio: "))
    area = math.pi * radio**2
    longitud = 2 * math.pi * radio
    
    print(f"El área es de {round(area, 2)}")
    print(f"La longitud es de {round(longitud, 2)}")

if __name__ == "__main__":
    obtenerRadioYLongitud()