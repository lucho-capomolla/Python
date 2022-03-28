import cv2 as cv
import numpy as np
import os

ruta = "FotosPrueba"
rutaCarpeta = "D:/Data User/Desktop/Cursos/Curso Python/Scripts/Reconocimiento Facial/Data"
rutaCompleta = rutaCarpeta + "/" + ruta
# Archivo que sirve para discriminar los ruidos o valores que no nos interesa tomar
ruidos = cv.CascadeClassifier("D:\Data User\Desktop\Cursos\Curso Python\Scripts\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml")

# Datos:
#  Poniendo 0: Toma la Cámara Web y hace el reconocimiento desde ahi
#  Poniendo 1: Utiliza la cámara del celular, mediante DroidCam
#  Poniendo una ruta puede hacer el reconocimiento a un video
camara = cv.VideoCapture(0)

if not os.path.exists(rutaCompleta):
    os.makedirs(rutaCompleta)

id = 0
while True:
    respuesta, captura = camara.read()
    if respuesta == False:
        break
    
    grises = cv.cvtColor(captura, cv.COLOR_BGR2GRAY)
    idCaptura = captura.copy()
    
    cara = ruidos.detectMultiScale(grises, 1.3, 5)
    
    for (x,y,e1,e2) in cara:
        cv.rectangle(captura, (x,y), (x+e1,y+e2), (0,255,0), 2)
        rostroCapturado = idCaptura[y:y+e2, x:x+e1]
        rostroCapturado = cv.resize(rostroCapturado, (160,160), interpolation=cv.INTER_CUBIC)
        cv.imwrite(rutaCompleta+"/imagen_{}.jpg".format(id), rostroCapturado)
        id += 1
        
    cv.imshow("Resultado rostro", captura)
    
    """if cv.waitKey(1) == ord("q"):
        break """
    
    # Llega hasta 100 rostros capturados
    if id == 350:
        break
camara.release()
cv.destroyAllWindows
