# Creación de una ventana para llenar con texto

from tkinter import *

ventana = Tk()
ventana.title("Primera ventana con Python")
# Para poder agrandar (Horizontal, Vertical)
ventana.resizable(True, True)
#ventana.iconbitmap("icon.ico")
ventana.geometry("100x100")

frame = Frame()
frame.pack()

scrollY = Scrollbar(frame)
scrollY.pack(side=RIGHT, fill=Y)

texto = Text(frame)
texto.config(width=50, height=50, bg="grey")
texto.pack(expand=YES, fill=BOTH)
texto.insert(0.0, "Texto inicial")
texto.config(yscrollcommand=scrollY.set)
scrollY.config(command=texto.yview)

# Tiene que estar siempre, para lanzar la ventana
ventana.mainloop()