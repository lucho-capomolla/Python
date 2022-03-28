# Creación de una ventana con Option


from tkinter import *
from turtle import width

def click():
    cadena = "Pulsaste "
    if(opcion.get()==1):
        cadena += "Rojo"
        ventana.config(bg="red")
    elif(opcion.get()==2):
        cadena += "Azul"
        ventana.config(bg="blue")
    elif(opcion.get()==3):
        cadena += "Verde"
        ventana.config(bg="green")
    etiqueta.config(text=cadena)


# Constantes // Con esto se pueden manejar las dimensiones de la Ventana
ANCHO = 640
ALTO = 360
POSX = 200
POSY = 300
anchoAlto = str(ANCHO)+"x"+str(ALTO)
posicionX = "+"+str(POSX)
posicionY = "+"+str(POSY)



ventana = Tk()
ventana.title("OptionButton")
# Para poder agrandar (Horizontal, Vertical)
ventana.resizable(True, True)
#ventana.iconbitmap("icon.ico")
ventana.geometry(anchoAlto+posicionX+posicionY)
ventana.config()

frame = Frame()
frame.pack()
frame.config()

opcion = IntVar()
rbdRojo = Radiobutton(frame, text="Rojo", variable=opcion, value=1, command=click)
rbdRojo.grid(column=1, row=3)
rbdAzul = Radiobutton(frame, text="Azul", variable=opcion, value=2, command=click)
rbdAzul.grid(column=1, row=4)
rbdVerde = Radiobutton(frame, text="Verde", variable=opcion, value=3, command=click)
rbdVerde.grid(column=1, row=5)

etiqueta = Label(frame, text="Selecciona una opción")
etiqueta.grid(column=1, row=1)

# Tiene que estar siempre, para lanzar la ventana
ventana.mainloop()