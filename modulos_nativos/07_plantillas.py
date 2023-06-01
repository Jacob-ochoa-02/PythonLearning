from email.mime.multipart import MIMEMultipart
# Multipurpose internet mail extension -> MIME
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from string import Template
from pathlib import Path
import smtplib

plantilla = Path("modulos_nativos/plantilla.html").read_text("utf-8")
template = Template(plantilla)
# cuerpo = template.substitute({"usuario": "Leonsito Feliz"})
cuerpo = template.substitute(usuario="Leonsito Feliz")
# .substitute -> Permite remplazar las variables de la plantilla
path = Path("modulos_nativos/holamundo.png")
mensaje = MIMEMultipart()
mime_Image = MIMEImage(path.read_bytes())
mensaje["from"] = "Hola Mundo"
mensaje["to"] = "jacobo_ochoa95192@elpoli.edu.co"
mensaje["subject"] = "Esta es una prueba"
cuerpo = MIMEText(cuerpo, "html")
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
