# OpenCV: análisis de imágenes
import cv2 as cv
from cv2 import threshold

imagen = cv.imread('contorno.jpg')
# Transforma la imagen en una escala de grises
escalaGrises = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
# Recibe la imagen ya transformada en grises, un rango de colores, y un umbral
#tipoUmbral, umbral = cv.threshold(escalaGrises, 100,255, cv.THRESH_BINARY)
#   Se usa _ porque no interesa utilizar esa variable que retorna la función
_, umbral = cv.threshold(escalaGrises, 100,255, cv.THRESH_BINARY)

contornos, jerarquia = cv.findContours(umbral, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# - aprox_none: obtiene todos los puntos del contorno (usa mas puntos)
# - aprox_simple: elimina puntos redundantes (ubica vertices o puntos claves), de forma mas aproximada (menos puntos, ahorra memoria)

# drawContours(imagen, contornos(dada por threshold), capaContorno, RGB, grosorContorno)
# - CapaContorno: -1: agarra todos los contornos, en adelante va eligiendo los demás contornos
cv.drawContours(imagen, contornos, -1, (255,50,50), 2)

# Mostrar imagen
cv.imshow('Imagen original', imagen)
#cv.imshow('Imagen en grises', escalaGrises)
#cv.imshow('Imagen con umbral', umbral)
#print(f"Tipo de umbral trabajado: {tipoUmbral}")

#   - Para que no se cierre automáticamente la ventana emergente
cv.waitKey(0)
#   - Para cerrar todas las ventanas emergentes (por si hay mas de 1)
cv.destroyAllWindows()


