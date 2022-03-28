# 8. Mostrar el importe del IVA de un articulo con un valor ingresado junto con su precio final.

def ejercicio08():
    IVA = 0.21
    precioBase = int(input("Ingrese el valor del artículo: "))
    precioFinal = precioBase + (precioBase * IVA)
    print(f"El precio final del artículo es de {precioFinal}")

# Para ejecutar el programa
ejercicio08()