# Previamente, si utilizamos una cuenta de Gmail hay que activar dentro
# de Seguridad la opción para que se pueda Acceder a aplicaciones poco seguras

import smtplib

def enviar(remitente, destinatario, mensaje):
    usuario = remitente
    password = "password1234"
    
    try:
        conexion = smtplib.SMTP("smtp.gmail.com", 587)
        conexion.starttls()
        conexion.login(usuario, password)
        print("Login correcto.")
        conexion.sendmail(remitente, destinatario, mensaje)
        print("Email enviado correctamente")
        conexion.quit()
    except smtplib.SMTPAuthenticationError:
        print("Error de autenticación.")
        
if __name__ == "__main__":
    enviar("emailRemitente@gmail.com", "emailDestinatario@gmail.com", "Mensaje a enviar")