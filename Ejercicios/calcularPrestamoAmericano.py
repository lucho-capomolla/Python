import pandas as pd

def obtenerInteresEquivalente(interes, tiempo):
    interes = interes / 100
    interesEquivalente = ((1+interes)**(1/tiempo))-1
    return round(interesEquivalente*100,2)

def obtenerInteresPagado(capitalPendiente, interes):
    return (capitalPendiente*(interes/100))

def prestamoAmericano(capital, interes, tiempo):
    capitalPendiente = capital
    lista = []
    columnas = ['Período', 'Capital amortizado', 'Interes pagado', 'Capital pendiente']
    for i in range(1,tiempo+1):
        interesPagado = obtenerInteresPagado(capitalPendiente, interes)
        if i == tiempo:
            capitalAmortizado = capital
        else:
            capitalAmortizado = 0
        capitalPendiente -= capitalAmortizado 
        lista.append([i, round(capitalAmortizado, 2),
                      round(interesPagado, 2),
                      round(capitalPendiente, 2)])
    prestamo = pd.DataFrame(lista, columns=columnas)
    prestamo.set_index('Período', inplace=True)
    return prestamo

if __name__ == "__main__":
    cuadro = prestamoAmericano(6000, 17, 6)
    print(cuadro)
        
        
        