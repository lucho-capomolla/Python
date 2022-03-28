# Creación de una ventana con Spinbox

from tkinter import *
from tkinter import messagebox

def mostrar():
    messagebox.showinfo("Mensaje", "El valor seleccionado es: " + valor.get())

ventana = Tk()
ventana.title("Ventana emergente")
ventana.resizable(True, True)
#ventana.iconbitmap("icon.ico")
ventana.geometry("640x520")
valor = StringVar()
etiqueta = Label(ventana, text="Spinbox").place(x=20, y=20)
combo = Spinbox(ventana,from_=1,to=10,textvariable=valor).place(x=20,y=60)
boton = Button(ventana, text="Valor", command=mostrar).place(x=20,y=100)
ventana.mainloop()