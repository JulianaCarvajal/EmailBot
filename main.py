import os
import smtplib
import ssl

from email.message import EmailMessage
from dotenv import load_dotenv
# Trying to import subject and body
try:
    from email_content import subject, body
except ImportError:
    raise RuntimeError("The email_content.py file with the subject and body of the message is missing.")

def creds_setup():
    """
    Get credentials from .env file.

    :return: Dictionary with credentials
    """
    load_dotenv()
    return {
        'sender': os.getenv("EMAIL_ADDRESS"),
        'receivers': [os.getenv("EMAIL_RECEIVER")],
        'bcc': [os.getenv("EMAIL_ADDRESS")],
        'password': os.getenv("EMAIL_PASS")
    }

def create_message(receivers, sender, subject, body):
    """
    Create EmailMessage object.

    :param receivers: Receiver(s) email(s)
    :param sender: Sender email
    :param subject: Email subject
    :param body: Email body
    :return: EmailMessage object
    """
    msg = EmailMessage()
    msg["To"] = ", ".join(receivers)
    msg["From"] = sender
    msg["Subject"] = subject
    msg.set_content(body)
    return msg

def send_message(host, port, sender, password, receivers, msg, bcc=[]):
    """
    Send message through SMTP.

    :param host: SMTP server
    :param port: SMTP server port
    :param sender: Sender email
    :param password: Sender password
    :param receivers: Receiver(s) email(s)
    :param msg: EmailMessage object
    :param bcc: Bcc receivers (optional)
    """
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receivers + bcc, msg.as_string())

def main():
    """
    Main function.
    Construct the message and send it.
    """
    creds = creds_setup()
    email_subject, email_body = subject, body
    msg = create_message(creds['receivers'], creds['sender'], email_subject, email_body)
    send_message("smtp.gmail.com", 465, creds['sender'], creds['password'], creds['receivers'], msg, creds['bcc'])

if __name__ == "__main__":
    main()