# MIME > 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from validate_email import validate_email
from smtplib import SMTP
from os import environ


def cambiarPassword(destinatario):
    existeEmail = validate_email(destinatario)

    if not existeEmail:
        print('el correo no existe')
        return

    texto = '''Hola, has cambiado la contraseña si no fuiste tu comunicate con 
    nosotros, caso contrario obvia el mensaje'''
    emailEmisor = environ.get('CORREO_EMISOR')
    passwordEmisor = environ.GET('PASSWORD_EMISOR')

    cuerpo = MIMEText(texto, 'plain')

    correo = MIMEMultipart()
    correo['Subject'] = 'Cambiaste la contraseña'
    correo['To'] = destinatario

    correo.attach(cuerpo)

    emisor = SMTP('smtp.gmail.com', 587)
    emisor.starttls()
    emisor.login(emailEmisor, passwordEmisor)
    emisor.sendmail(from_addr=emailEmisor, to_addres=destinatario, msg=correo.as_string())
    emisor.quit()
    print('Correo enviado')













































