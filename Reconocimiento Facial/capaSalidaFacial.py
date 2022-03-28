import cv2 as cv
import os

rutaData = "D:/Data User/Desktop/Cursos/Curso Python/Scripts/Reconocimiento Facial/Data"
listaData = os.listdir(rutaData)

entrenamientoEigenFaceRecognizer = cv.face.EigenFaceRecognizer_create()
entrenamientoEigenFaceRecognizer.read("EntrenamientoEigenFaceRecognizer.xml")
ruidos = cv.CascadeClassifier("D:\Data User\Desktop\Cursos\Curso Python\Scripts\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml")
camara = cv.VideoCapture(0)
#camara = cv.VideoCapture("videoauron.mp4")
#camara = cv.VideoCapture("ElonMusk.mp4")

while True:
    respuesta, captura = camara.read()
    
    if respuesta == False:
        break
    
    grises = cv.cvtColor(captura, cv.COLOR_BGR2GRAY)
    idCaptura = grises.copy()
    cara = ruidos.detectMultiScale(grises, 1.3, 5)
    for (x,y,e1,e2) in cara:
        rostroCapturado = idCaptura[y:y+e2, x:x+e1]
        rostroCapturado = cv.resize(rostroCapturado, (160,160), interpolation=cv.INTER_CUBIC)
        resultado = entrenamientoEigenFaceRecognizer.predict(rostroCapturado)
        cv.putText(captura, "{}".format(resultado), (x,y-5), 1,1.3, (0,255,0), 1, cv.LINE_AA)
        if resultado[1] < 8000:
            cv.putText(captura, "{}".format(listaData[resultado[0]]), (x,y+15), 1,1.3, (0,255,0), 1, cv.LINE_AA)
            cv.rectangle(captura, (x,y), (x+e1, y+e2), (0,255,0), 2)
        else:
            cv.putText(captura, "No encontrado", (x,y+15), 1,1.3, (0,255,0), 1, cv.LINE_AA)
            cv.rectangle(captura, (x,y), (x+e1, y+e2), (0,255,0), 2)

    cv.imshow("Resultados", captura)    
    if cv.waitKey(1) == ord("q"):
        break
camara.release()
cv.destroyAllWindows()    
        
        
        