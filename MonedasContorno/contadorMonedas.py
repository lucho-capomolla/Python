import cv2 as cv
import numpy as np

original = cv.imread("monedas.jpg")
escalaGrises = cv.cvtColor(original, cv.COLOR_BGR2GRAY)

valorGauss = 3
valorKernel = 3
# GaussianBlur : suavizado para imagenes borrosas o ruidosas (agregando mas pixeles)
gauss = cv.GaussianBlur(escalaGrises, (valorGauss, valorGauss), 0)

# Usa el modelado de gauss habiendo eliminado todo el ruido, y así con Canny
#       poder delimitar los contornos de la imagen.
canny = cv.Canny(gauss, 60, 100)

# Genera una matriz
kernel = np.ones((valorKernel, valorKernel), np.uint8)

# En este caso, usa una morfologia de clausura, para poder eliminar el
#   ruido que se encuentra dentro del contorno, y asi quedarse con el contorno exterior
cierre = cv.morphologyEx(canny, cv.MORPH_CLOSE, kernel)

contornos, jerarquia = cv.findContours(cierre.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print("Monedas encontradas: {}".format(len(contornos)))

cv.drawContours(original, contornos, -1, (255,50,50), 2)

# Mostrar resultado
cv.imshow("Monedas", original)
#cv.imshow("Escala Grises", escalaGrises)
#cv.imshow("Modelado Gauss", gauss)
#cv.imshow("Canny", canny)
cv.waitKey(0)