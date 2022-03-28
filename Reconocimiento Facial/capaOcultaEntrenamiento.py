from cProfile import label
import cv2 as cv
import numpy as np
import os
from time import time

rutaData = "D:/Data User/Desktop/Cursos/Curso Python/Scripts/Reconocimiento Facial/Data"
listaData = os.listdir(rutaData)
print("Data", listaData)
ids = []
rostrosData = []
id = 0
tiempoInicial = time()
for fila in listaData:
    rutaCompleta = rutaData + "/" + fila
    print("Iniciando lectura...")
    
    for archivo in os.listdir(rutaCompleta):
        print("Imagenes: ", fila + "/" + archivo)
        ids.append(id)
        rostrosData.append(cv.imread(rutaCompleta + "/" + archivo, 0))
        #imagenes = cv.imread(rutaCompleta + "/" + archivo, 0)
        
    id += 1
    tiempoFinalLectura = time()
    tiempoTotalLectura = tiempoFinalLectura + tiempoInicial
    print("Tiempo total lectura: ", tiempoTotalLectura)
    
entrenamientoEigenFaceRecognizer = cv.face.EigenFaceRecognizer_create()
print("Iniciando el entrenamiento...")
entrenamientoEigenFaceRecognizer.train(rostrosData, np.array(ids))
tiempoFinalEntrenamiento = time()
tiempoTotalEntrenamiento = tiempoFinalEntrenamiento + tiempoTotalLectura
print("Tiempo total entrenamiento: ", tiempoTotalEntrenamiento)
entrenamientoEigenFaceRecognizer.write("EntrenamientoEigenFaceRecognizer.xml")
print("Entrenamiento concluido")
