# Variables de entorno
# SENDGRID_API_KEY = "edewfewfjewefefwflkwflwfw"

import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

apikey = os.environ.get("SENDGRID_API_KEY")
email = os.environ.get("SENDGRID_EMAIL")

mensaje = Mail(
    from_email=email,
    to_emails=email,
    subject="Correo de Prueba",
    html_content="Curso de <b>Ultimate Python</b>"
)

try:
    apikey = os.environ.get("SENDGRID_API_KEY")
    sg = SendGridAPIClient(apikey)
    respuesta = sg.send(mensaje)
    print(
        respuesta.status_code,  # para saber el código de respuesta del servidor
        respuesta.body,     # para saber el texto o mensaje que me devuelve el servidor
        respuesta.headers,  # cabeceras
    )
except Exception as e:
    print(e)
