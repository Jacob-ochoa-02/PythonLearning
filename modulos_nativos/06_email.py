from email.mime.multipart import MIMEMultipart
# Multipurpose internet mail extension -> MIME
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

path = Path("modulos_nativos/hola.png")
mensaje = MIMEMultipart()
mime_Image = MIMEBase(path.read_bytes())
mensaje["from"] = "Jacob"
mensaje["to"] = "a.sergio62@yahoo.es"
mensaje["subject"] = "Hola pa"
cuerpo = MIMEText("Hola, pa")
mensaje.attach(cuerpo)
mensaje.attach(mime_Image)


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    # ehlo-> identificarnos con el servidor smtp
    # identificar el nombre del dominio que usaremos para enviar los correos
    smtp.starttls()
    # tls -> transport layer security - se enviaran los correos encriptados
    smtp.login("jacobo_ochoa95192@elpoli.edu.co", "jacobo8alopera")
    smtp.send_message(mensaje)
    print("mensaje enviado")
