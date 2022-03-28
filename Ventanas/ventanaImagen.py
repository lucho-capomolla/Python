# Creación de una ventana con una imagen dentro

from tkinter import *
from PIL import ImageTk, Image

ventana = Tk()
ventana.title("Primera ventana con Python")
# Para poder agrandar (Horizontal, Vertical)
ventana.resizable(True, True)
ventana.iconbitmap("icon.ico")
ventana.geometry("800x600")

imagen = ImageTk.PhotoImage(Image.open("icon.ico"))
imglabel = Label(ventana, image=imagen).place(x=0,y=0)


# Tiene que estar siempre, para lanzar la ventana
ventana.mainloop()