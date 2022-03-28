# Creación de ventana con etiqueta

from tkinter import *

def click():
    texto = entrada.get()
    etiqueta.configure(text=texto)


ventana = Tk()
ventana.title("Widgets básicos")
# Para poder agrandar (Horizontal, Vertical)
ventana.resizable(True, True)
#ventana.iconbitmap("icon.ico")
ventana.geometry("640x360")
frame = Frame()
frame.pack()
frame.config(width="640", height="360")

# - Etiqueta
etiqueta = Label(frame, text="Etiqueta", font=("Arial", 20))
    # Coloca la etiqueta en función a X e Y
#etiqueta.place(x=100, y=100)
    # Coloca la etiqueta en función a Columnas y Filas
etiqueta.grid(column=1, row=2)

# - Boton
boton = Button(frame, text="Pulsar", font=("Arial", 15), background="Blue", foreground="Yellow", command=click)
boton.grid(column=1, row=5)

# - Entrada
entrada = Entry(frame, width=50)
entrada.grid(column=1, row=3)

# Tiene que estar siempre, para lanzar la ventana
ventana.mainloop()