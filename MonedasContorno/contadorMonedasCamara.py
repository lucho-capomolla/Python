import cv2 as cv
import numpy as np

def ordenarPuntos(puntos):
    n_puntos = np.concatenate(puntos[0], puntos[1], puntos[2], puntos[3]).tolist()
    y_order = sorted(n_puntos, key=lambda n_puntos: n_puntos[1])
    x1_order = y_order[:2]
    x1_order = sorted(x1_order, key=lambda x1_order: x1_order[0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key=lambda x2_order: x2_order[0])
    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]

def alineamiento(imagen, ancho, alto):
    imagen_alineada = None
    grises = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    tipoUmbral, umbral = cv.threshold(grises, 150, 255, cv.THRESH_BINARY)
    cv.imshow("Umbral", umbral)
    contorno, jerarquia = cv.findContours(umbral, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
    contorno = sorted(contorno, key=cv.contourArea, reverse=True)[:1]
    for curva in contorno:
        epsilon = 0.01 * cv.arcLength(curva, True)
        aprox = cv.approxPolyDP(curva, epsilon, True)
        if len(aprox) == 4:
            puntos = ordenarPuntos(aprox)
            puntos1 = np.float32(puntos)
            # Las 4 esquinas
            puntos2 = np.float32([[0,0], [ancho, 0], [0, alto], [ancho, alto]])
            perspectiva = cv.getPerspectiveTransform(puntos1, puntos2)
            imagen_alineada = cv.warpPerspective(imagen, perspectiva, (ancho, alto))
    return imagen_alineada


capturaVideo = cv.VideoCapture(1)

if not capturaVideo.isOpened():
    print("No se ha encontrado una cámara.")
    exit()
else:
    while True:
        tipoCamara, camara = capturaVideo.read()
        
        if tipoCamara == False:
            break
        
        # Para Ancho y Alto tienen que ser en pixeles
        imagen_A6 = alineamiento(camara, ancho=480, alto=677)
        
        if imagen_A6 is not None:
            puntos = []
            imagen_grises = cv.cvtColor(imagen_A6, cv.COLOR_BGR2GRAY)
            blur = cv.GaussianBlur(imagen_grises, (5,5), 1)
            _, umbral2 = cv.threshold(blur, 0, 255, cv.THRESH_OTSU+cv.THRESH_BINARY_INV)
            cv.imshow("Umbral", umbral2)
            contorno2, jerarquia2 = cv.findContours(umbral2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
            cv.drawContours(imagen_A6, contorno2, -1, (255,0,0), 2)
            suma1 = 0.0
            suma2 = 0.0
            
            for c_2 in contorno2:
                area = cv.contourArea(c_2)
                Momentos = cv.moments(c_2)
                if(Momentos["m00"]==0):
                    Momentos["m00"] = 1.0
                x = int(Momentos["m10"] / Momentos["m00"])
                y = int(Momentos["m01"] / Momentos["m00"])
                
                if area < 9800 and area > 7000:
                    fuente = cv.FONT_HERSHEY_SIMPLEX
                    cv.putText(imagen_A6, "$10", (x,y), fuente, 0.75, (0,255,0), 2)
                    suma1 += 10
                elif area < 7000 and area > 6500:
                    fuente = cv.FONT_HERSHEY_SIMPLEX
                    cv.putText(imagen_A6, "$1", (x,y), fuente, 0.75, (0,255,0), 2)
                    suma2 += 1
            total = suma1 + suma2
            print(f"Sumatoria total $: {total}")
            cv.imshow("Imagen A6", imagen_A6)
            cv.imshow("Umbral", camara)
            
        if cv.waitKey(1) == ord("q"):
            break
        
    capturaVideo.release()
    cv.destroyAllWindows()