from tkinter import *
from tkinter import messagebox
from baseDatos import *

# Constantes y Variables
ANCHO = 560
ALTO = 540
POSX = 400
POSY = 400
anchoAlto = str(ANCHO)+"x"+str(ALTO)
posicionX = "+"+str(POSX)
posicionY = "+"+str(POSY)
colorVentana = "blue"
colorFondo = "blue"
colorLetra = "white"

# Funciones
def mostrarMensaje(titulo, mensaje):
    messagebox.showinfo(titulo, mensaje)
    
def mostrar():
    listado = consultar()
    text.delete(1.0, END)
    text.insert(INSERT, "ID\tNombre\tApellido\tTelefono\tEmail\n")
    for elemento in listado:
        id = elemento[0]
        nombre = elemento[1]
        apellido = elemento[2]
        telefono = elemento[3]
        email = elemento[4]
        text.insert(INSERT, id)
        text.insert(INSERT, "\t")
        text.insert(INSERT, nombre)
        text.insert(INSERT, "\t")
        text.insert(INSERT, apellido)
        text.insert(INSERT, "\t")
        text.insert(INSERT, telefono)
        text.insert(INSERT, "\t")
        text.insert(INSERT, email)
        text.insert(INSERT, "\n")
        
def limpiarDatos():
    id.set("")
    nombre.set("")
    apellido.set("")
    telefono.set("")
    email.set("")
    text.delete(1.0, END)
    
def guardar():
    crearTabla()
    if((nombre.get()=="") or apellido.get()==""):
        mostrarMensaje("Error", "Debes rellenar los datos")
    else:
        datos = nombre.get(), apellido.get(), telefono.get(), email.get()
        mostrarMensaje("Guardar", "Contacto guardado")
        insertar(datos)
        limpiarDatos()
        mostrar()

def actualizar():
    crearTabla()
    if(id.get() == "") or (id.get()==0) or (nombre.get() == ""):
        mostrarMensaje("Error", "Debes rellenar los datos")
    else:
        try:
            modificar(id.get(), nombre.get(), apellido.get(), telefono.get(), email.get())
            mostrarMensaje("Modificar", "Contacto modificado")
            limpiarDatos()
            mostrar()
        except:
            mostrarMensaje("Error", "Identificador no encontrado")
        
def eliminar():
    if(id.get() == "") or (id.get() == 0):
        mostrarMensaje("Error", "Debes insertar un identificador")
    else:
        try:
            borrar(id.get())
            mostrarMensaje("Borrar", "Contacto borrado")
            limpiarDatos()
            mostrar()
        except:
            mostrarMensaje("Error", "Identificador no encontrado")
            
def buscar():
    if(id.get() == "") or (id.get() == 0):
        mostrarMensaje("Error", "Debes insertar un identificador válido")
    else:
        contactos = consultarXid(id.get())
        for contacto in contactos:
            id.set(contacto[0])
            nombre.set(contacto[1])
            apellido.set(contacto[2])
            telefono.set(contacto[3])
            email.set(contacto[4])
        mostrarMensaje("Buscar", "Contacto encontrado")
    
      
# Ventana
ventana = Tk()
ventana.config(bg=colorVentana)
ventana.geometry(anchoAlto+posicionX+posicionY)
ventana.title("Agenda")
frame = Frame()
frame.config(width=ANCHO, height=ALTO)
frame.config(bg=colorVentana)
frame.pack()

# Variables
id = IntVar()
nombre = StringVar()
apellido = StringVar()
telefono = StringVar()
email = StringVar()

# Widgets
# - Etiquetas y Cajas
etiquetaID = Label(frame, text="ID: ").place(x=50, y=50)
cajaID = Entry(frame, textvariable=id).place(x=130, y=50)
etiquetaNombre = Label(frame, text="Nombre: ").place(x=50, y=90)
cajaNombre = Entry(frame, textvariable=nombre).place(x=130, y=90)
etiquetaApellido = Label(frame, text="Apellido: ").place(x=50, y=130)
cajaApellido = Entry(frame, textvariable=apellido).place(x=130, y=130)
etiquetaTelefono = Label(frame, text="Telefono: ").place(x=50, y=170)
cajaTelefono = Entry(frame, textvariable=telefono).place(x=130, y=170)
etiquetaEmail = Label(frame, text="Email: ").place(x=50, y=210)
cajaEmail = Entry(frame, textvariable=email).place(x=130, y=210)

text = Text(frame)
text.place(x=50, y=240, width=500, height=200)
# - Botones
botonAñadir = Button(frame, text="Añadir", 
                     command=guardar).place(x=150, y=500)
botonBorrar= Button(frame, text="Borrar", 
                    command=eliminar).place(x=200, y=500)
botonConsultar = Button(frame, text="Consultar", 
                        command=mostrar).place(x=250, y=500)
botonModificar= Button(frame, text="Actualizar", 
                       command=actualizar).place(x=320, y=500)
botonBuscar = Button(frame, text="Buscar", 
                     command=buscar).place(x=390, y=500)


ventana.mainloop()