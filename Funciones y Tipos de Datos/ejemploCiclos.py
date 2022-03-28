# WHILE
# - Tabla de Multiplicar:
tabla = int(input("Elija la tabla que se desea calcular: "))
print(f"Tabla del {tabla}")

contador = 1
while (contador < 11):
    resultado = tabla * contador
    # incrementar contador
    contador += 1
    # mostrar resultado
    print(f"{tabla} por {contador - 1} = {resultado}")
    
    
# FOR
# for 'variable' in 'rango de numeros'(inicio, total-1)
#for numero in range(1, 51):
    
# - Tabla de Multiplicar:
tabla = int(input("Elija la tabla que se desea calcular: "))
print(f"Tabla del {tabla}")

for contador in range(1,11):
    resultado = tabla * contador
    print(f"{tabla} por {contador} = {resultado}")
    
# - Ejemplo FOR con Lista
nombres = ["Pepe", "Cali", "Wachin"]
for nombre in nombres:
    print(f"Hola {nombre}")
    
# - Mostrar 100 primeros
for numero in range(1,101):
    print(numero)
    
