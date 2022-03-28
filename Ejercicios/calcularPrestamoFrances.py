import pandas as pd

def obtenerInteresEquivalente(interes, tiempo):
    interes = interes / 100
    interesEquivalente = ((1+interes)**(1/tiempo))-1
    return round(interesEquivalente*100,2)

def obtenerValorActual(interes, tiempo):
    interes = interes / 100
    valorActual = ((1-(1+interes)**(-tiempo))/interes)
    return valorActual

def obtenerInteresPagado(capitalPendiente, interes):
    return (capitalPendiente*(interes/100))

def prestamoFrances(capital, interes, tiempo):
    valorActual = obtenerValorActual(interes, tiempo)
    cuotaAmortizacion = capital / valorActual
    capitalPendiente = capital
    lista = []
    columnas = ['Período', 'Cuota amortización', 'Capital amortizado', 'Interes pagado', 'Capital pendiente']
    for i in range(1,tiempo+1):
        interesPagado = obtenerInteresPagado(capitalPendiente, interes)
        capitalAmortizado = cuotaAmortizacion - interesPagado
        capitalPendiente -= capitalAmortizado 
        lista.append([i, round(cuotaAmortizacion, 2), 
                      round(capitalAmortizado, 2),
                      round(interesPagado, 2),
                      round(capitalPendiente, 2)])
    prestamo = pd.DataFrame(lista, columns=columnas)
    prestamo.set_index('Período', inplace=True)
    return prestamo

if __name__ == "__main__":
    cuadro = prestamoFrances(1500, 12, 10)
    print(cuadro)
        
        
        