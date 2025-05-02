import re
import unicodedata
import requests
import os
from dotenv import load_dotenv

load_dotenv()
MAILERSEND_API_KEY = os.getenv("MAILERSEND_API_KEY")

FIXED_RECIPIENTS = [
    "didier.correa@proteccion.com.co",
    "correalondon@gmail.com",
    "jevojob@gmail.com"
]

def normalize_subject(subject: str) -> str:
    """Quita tildes y convierte a minúsculas."""
    nfkd = unicodedata.normalize("NFKD", subject)
    no_accents = "".join(c for c in nfkd if not unicodedata.combining(c))
    return no_accents.lower()

def is_technical_test(subject: str) -> bool:
    """
    Devuelve True si el asunto es del tipo:
      'Prueba Técnica – algo'
    (sin tilde, en minúsculas y con '-' o '–')
    """
    normalized = normalize_subject(subject)
    pattern = r"^prueba tecnica\s*[–-]\s*\S.+$"
    return bool(re.match(pattern, normalized))

def send_email_mailersend(
    to_email: str,
    subject: str,
    html_body: str,
    from_email: str,
    from_name: str
):
    """
    Envía correos por separado:
    - Si es “Prueba Técnica – Nombre”, manda un email individual
      a cada uno de FIXED_RECIPIENTS.
    - Siempre manda también un email al usuario original (to_email).
    - Si NO es “Prueba Técnica”, solo manda al usuario.
    """
    url = "https://api.mailersend.com/v1/email"
    headers = {
        "Authorization": f"Bearer {MAILERSEND_API_KEY}",
        "Content-Type": "application/json"
    }

    recipients = [to_email]

    if is_technical_test(subject):
        recipients.extend(FIXED_RECIPIENTS)

    responses = []
    for recipient in recipients:
        payload = {
            "from": {
                "email": from_email,
                "name": from_name
            },
            "to": [
                {"email": recipient}
            ],
            "subject": subject,
            "html": html_body
        }

        response = requests.post(url, json=payload, headers=headers)
        try:
            response.raise_for_status()
            responses.append({"email": recipient, "status": response.status_code})
        except requests.HTTPError as e:
            responses.append({
                "email": recipient,
                "status": response.status_code,
                "error": response.text
            })

    return responses


