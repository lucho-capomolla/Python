# Creación de una ventana con botones con ventanas emergentes

from tkinter import *
from tkinter import messagebox

def info():
    messagebox.showinfo("Mensaje", "Mensaje desde messagebox")

def advertencia():
    messagebox.showwarning("Mensaje", "Mensaje de Advertencia")

def pregunta():
    messagebox.askyesno("Mensaje", "¿Quieres continuar?")

ventana = Tk()
ventana.title("Ventana emergente")
ventana.resizable(True, True)
#ventana.iconbitmap("icon.ico")
ventana.geometry("360x320")

boton01 = Button(ventana, text="Info", command=info).place(x=20, y=100)
boton02 = Button(ventana, text="Advertencia", command=advertencia).place(x=20, y=140)
boton03 = Button(ventana, text="Pregunta", command=pregunta).place(x=20, y=180)
ventana.mainloop()