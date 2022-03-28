# Pasar ecuación a expresión algoritmica
# (c+5)(b^2 - 3ac)a^2 / 4a

def ejercicio20():

    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))

    resultado = ((c+5)*(b**2 - 3*a*c)*a**2)/(4*a)
    
    return resultado

print(ejercicio20())