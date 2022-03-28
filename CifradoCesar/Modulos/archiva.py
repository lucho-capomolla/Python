import pickle

def guarda(texto):
    fichero = open("datos.pckl", "wb")
    pickle.dump(texto, fichero)
    #print("Fichero guardado")
    fichero.close()
    
def carga():
    fichero = open("datos.pckl", "rb")
    datos = pickle.load(fichero)
    #print(datos)
    fichero.close()
    return datos

if __name__ == "__main__":
    guarda("Hola mundo")
    carga()