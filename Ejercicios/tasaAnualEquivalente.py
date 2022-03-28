
def obtenerTAE(interes, periodo):
    interes = interes / 100
    tae = ((1+(interes/periodo))**periodo) - 1
    tae = tae * 100
    return tae

if __name__ == "__main__":
    print(round(obtenerTAE(8,1),2))
    print(round(obtenerTAE(8,12),2))
    