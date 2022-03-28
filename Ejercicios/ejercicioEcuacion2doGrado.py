from math import sqrt

# Ecuación: ax^2 + bx + c = 0
def ecuacionSegundoGrado(a,b,c):
    x1 = 0
    x2 = 0
    parcial = (b**2) - (4*a*c)
    if(parcial > 0):
        x1 = (-b + sqrt(parcial)/(2*a))
        x2 = (-b - sqrt(parcial)/(2*a))
        return x1,x2
    else:
        x1 = 0
        x2 = 0
        print("No se puede resolver")
        return x1,x2
    
a = int(input("Ingrese el valor de 'a': "))
b = int(input("Ingrese el valor de 'b': "))
c = int(input("Ingrese el valor de 'c': "))
x1, x2 = ecuacionSegundoGrado(a,b,c)
print(f"La solución de X1 es {x1} y la de X2 es {x2}")
