# Creación de un ventana con CheckBox

from tkinter import *
from turtle import width

def click():
    cadena = "Pulsaste "
    if(color01.get()):
        cadena += "Rojo"
        ventana.config(bg="red")
    elif(color02.get()):
        cadena += "Azul"
        ventana.config(bg="blue")
    elif(color03.get()):
        cadena += "Verde"
        ventana.config(bg="green")
    elif(not color01.get() and not color02.get() and not color03.get()):
        cadena = "No hay nada pulsado"
        ventana.config(bg="white")
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

color01 = IntVar() # 1 o 0 
color02 = IntVar()
color03 = IntVar()

chkRojo = Checkbutton(frame, text="Rojo", variable=color01, onvalue=1, offvalue=0, command=click)
chkRojo.grid(column=1, row=2)
chkAzul = Checkbutton(frame, text="Azul", variable=color02, onvalue=1, offvalue=0, command=click)
chkAzul.grid(column=1, row=3)
chkVerde = Checkbutton(frame, text="Verde", variable=color03, onvalue=1, offvalue=0, command=click)
chkVerde.grid(column=1, row=4)


etiqueta = Label(frame, text="Selecciona una opción")
etiqueta.grid(column=1, row=1)

# Tiene que estar siempre, para lanzar la ventana
ventana.mainloop()