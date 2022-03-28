from tkinter import *
from tkinter import messagebox
from Modulos.archiva import *
from Modulos.cesar import *

# Funciones
def codificar():
    texto = textoSinCodificar.get()
    if texto != "":
        textoCodificado.set(codifica(texto))
        mensaje("Codificado", "Texto codificado!")
    else:
        mensaje("Error", "Error al codificar el texto")
    
def descodificar():
    texto = textoCodificado.get()
    if texto != "":
        textoSinCodificar.set(descodifica(texto))
        mensaje("Decodificar", "Texto decodificado!")
    else:
        mensaje("Error", "Error al decodificar el texto")

def grabar():
    texto = textoCodificado.get()
    if texto != "":
        guarda(texto)
        mensaje("Info", "Mensaje guardado")
    else:
        mensaje("Error", "Error al guardar el texto")

def cargar():
    try:
        textoCodificado.set(carga())
        descodificar()
    except:
        mensaje("Error", "Error al cargar el archivo")

def borrar():
    textoCodificado.set("")
    textoSinCodificar.set("")

def mensaje(titulo, mensaje):
    messagebox.showinfo(titulo, mensaje)


# Ventana
ventana = Tk()
ventana.title("Cifrado Cesar")
ventana.config(bg="grey")
ventana.geometry("380x380")
ventana.config(relief="sunken")  
ventana.config(bd=25)              

frame = Frame()
frame.config(width=380, height=380)
frame.config(bg="grey")
frame.pack(fill="both", expand=True, padx=20, pady=20)

# Etiquetas y Cajas
textoSinCodificar = StringVar()
textoCodificado = StringVar()
etiquetaSinCodificar = Label(frame, 
                             text="Texto sin codificar:").grid(row=3, column=2)
cajaSinCodificar = Entry(frame, 
                         textvariable=textoSinCodificar).grid(row=3, column=4)
etiquetaCodificado = Label(frame, 
                          text="Texto codificado").grid(row=6, column=2)
cajaCodificado = Entry(frame, 
                       textvariable=textoCodificado).grid(row=6,column=4)

# Botones
botonCodificar = Button(frame, text="Codificar", 
                        command=codificar).grid(row=9,column=2)
botonDescodificar = Button(frame, text="Descodificar", 
                           command=descodificar).grid(row=9,column=4)
botonGrabar = Button(frame, text="Grabar", 
                     command=grabar).grid(row=12,column=2)
botonCargar = Button(frame, text="Cargar", 
                     command=cargar).grid(row=12,column=4)
botonBorrar = Button(frame, text="Borrar", 
                     command=borrar).grid(row=15,column=2)

ventana.mainloop()