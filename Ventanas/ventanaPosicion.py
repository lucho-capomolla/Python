# Creación de una ventana con entradas de texto 

from tkinter import *
from turtle import width

def click():
    texto = nombre.get()+", "+str(edad.get())+" años"
    etiquetaResultado.configure(text=texto)

# Constantes // Con esto se pueden manejar las dimensiones de la Ventana
ANCHO = 550
ALTO = 400
POSX = 200
POSY = 300
anchoAlto = str(ANCHO)+"x"+str(ALTO)
posicionX = "+"+str(POSX)
posicionY = "+"+str(POSY)

ventana = Tk()
ventana.title("Posicionando ventana")
# Para poder agrandar (Horizontal, Vertical)
ventana.resizable(True, True)
#ventana.iconbitmap("icon.ico")
ventana.geometry(anchoAlto+posicionX+posicionY)
ventana.config()

frame = Frame()
frame.pack()
frame.config()

# Variables
nombre = StringVar()
edad = IntVar()

etiquetaNombre = Label(frame, text="Nombre", font=("Arial", 12))
etiquetaNombre.grid(column=1, row=2)
entradaNombre = Entry(frame, textvariable=nombre, width=50)
entradaNombre.grid(column=2, row=2)

etiquetaEdad = Label(frame, text="Edad", font=("Arial", 12))
etiquetaEdad.grid(column=1, row=3)
entradaEdad = Entry(frame, textvariable=edad, width=50)
entradaEdad.grid(column=2, row=3)
edad.set("")
etiquetaResultado = Label(frame, text="", font=("Arial", 12))
etiquetaResultado.grid(column=2, row=7)
boton = Button(frame, text="Pulsar", bg="blue", fg="yellow", command=click)
boton.grid(column=2, row=5)

# Tiene que estar siempre, para lanzar la ventana
ventana.mainloop()