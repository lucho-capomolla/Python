import cv2 as cv

# En 0: Camaras que esten trabajando en la PC
# En 1: Camaras externas (camaras de seguridad)
# En mi caso, utilizo 1 porque con 0 toma la WebCam
capturaVideo = cv.VideoCapture(1)

if not capturaVideo.isOpened():
    print("No se ha encontrado una cámara.")
    exit()
else:
    while True:
        _, camara = capturaVideo.read()
        grises = cv.cvtColor(camara, cv.COLOR_BGR2GRAY)
        
        cv.imshow("En vivo", grises)
        if cv.waitKey(1) == ord("q"):
            break
    capturaVideo.release()
    cv.destroyAllWindows()