from tkinter import *

ventana = Tk()
ventana.title("Primera ventana con Python")
# Para poder agrandar (Horizontal, Vertical)
ventana.resizable(True, True)
ventana.iconbitmap("icon.ico")
ventana.geometry("800x600")
ventana.config(background="grey")
frame = Frame()
frame.pack(side="top", anchor="s")
frame.config(background="blue")
frame.config(width="640", height="360")
# Tiene que estar siempre, para lanzar la ventana
ventana.mainloop()