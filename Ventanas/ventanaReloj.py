# Creación de una ventana implementando la libreria 'time' para agregar un reloj

import tkinter as tk
import time

class Ventana():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("640x420")
        # Permite redimensionar siempre que este en True
        self.ventana.resizable(True,True)
        self.ventana.title("Reloj")
        self.ventana.config(background="blue")
        self.etiqueta = tk.Label(text="Etiqueta", 
                                 font=("Arial", 20), 
                                 foreground="blue", 
                                 background="yellow",
                                 pady=15,
                                 padx=15)
        self.etiqueta.place(x=190, y=150)
        self.actualizacion()        
        self.ventana.mainloop()

    def actualizacion(self):
        hora = time.strftime("%H:%M:%S")
        self.etiqueta.configure(text=hora)
        self.ventana.after(1000, self.actualizacion)

if __name__ == "__main__":
    main = Ventana()