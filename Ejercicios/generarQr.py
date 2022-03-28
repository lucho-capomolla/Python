import qrcode

nombreArchivo = input("Ingrese el nombre del archivo: ")
textoQr = input("Ingrese el enlace para el código QR: ")

imagen = qrcode.make(textoQr)
fichero = open(nombreArchivo+".png", "wb")
imagen.save(fichero)
fichero.close()
print("El código QR ha sido generado.")
