# Creación de una ventana con una Barra de Menú

from tkinter import *
from tkinter import messagebox

def salir():
    opcion = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if opcion == "yes":
        ventana.destroy()

ventana = Tk()
ventana.title("Ventana con Menú")
ventana.resizable(True, True)
#ventana.iconbitmap("icon.ico")
ventana.geometry("640x520")
barraMenu = Menu(ventana)
ventana.config(menu=barraMenu)

menuArchivo = Menu(barraMenu, tearoff=0)
menuArchivo.add_command(label="Abrir")
menuArchivo.add_command(label="Salir", command=salir)
menuAyuda = Menu(barraMenu, tearoff=0)
menuAyuda.add_command(label="Acerca de")

barraMenu.add_cascade(label="Archivo", menu=menuArchivo)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)


ventana.mainloop()