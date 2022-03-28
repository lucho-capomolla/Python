from tkinter import *
from tkinter import messagebox
from enviarEmail import enviar

def mostrarMensaje(titulo, mensaje):
    messagebox.showinfo(titulo, mensaje)

def enviarMensaje():
    remitente = "mailRemitente@gmail.com"
    mensaje = textoMensaje.get(1.0,END)
    enviar(remitente, destinatario.get(), mensaje)
    borrarMensaje()
    mostrarMensaje("Aviso", "Email enviado")

def borrarMensaje():
    destinatario.set("")
    textoMensaje.delete(1.0, END)


ventana = Tk()
ventana.geometry("640x520")
ventana.resizable(0,0)
ventana.title("Email")
ventana.config(background="blue")
destinatario = StringVar()
etiquetaDestinatario = Label(ventana, 
                             text="Destinatario", 
                             font=("Arial", 12),
                             bg="white", 
                             fg="blue",
                             pady=5,
                             padx=5)
etiquetaDestinatario.place(x=10,y=10, width=100)
textoDestinatario = Entry(ventana, textvariable=destinatario).place(x=120,y=10,width=300)
etiquetaMensaje = Label(ventana, 
                             text="Mensaje", 
                             font=("Arial", 12),
                             bg="white", 
                             fg="blue",
                             pady=5,
                             padx=5)
etiquetaMensaje.place(x=10,y=50, width=100)
textoMensaje = Text(ventana)
textoMensaje.place(x=120, y=50,width=300)
botonEnviar = Button(ventana, text="Enviar", command=enviarMensaje).place(x=95,y=480)
botonBorrar = Button(ventana, text="Borrar", command=borrarMensaje).place(x=495,y=480)
ventana.mainloop()