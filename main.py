import os
import smtplib
import ssl

from email.message import EmailMessage
from dotenv import load_dotenv

def creds_setup():
    load_dotenv()
    return {
        'sender': os.getenv("EMAIL_ADDRESS"),
        'receivers': [os.getenv("EMAIL_RECEIVER")],
        'bcc': [os.getenv("EMAIL_ADDRESS")],
        'password': os.getenv("EMAIL_PASS")
    }

def create_message(receivers, sender, subject, body):
    msg = EmailMessage()
    msg["To"] = ", ".join(receivers)
    msg["From"] = sender
    msg["Subject"] = subject
    msg.set_content(body)
    return msg

def send_message(host, port, sender, password, receivers, msg, bcc=[]):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receivers + bcc, msg.as_string())

def main():
    creds = creds_setup()

    subject = "Test 5"
    body = "Receivers list?"

    msg = create_message(creds['receivers'], creds['sender'], subject, body)

    send_message("smtp.gmail.com", 465, creds['sender'], creds['password'], creds['receivers'], msg, creds['bcc'])

if __name__ == "__main__":
    main()