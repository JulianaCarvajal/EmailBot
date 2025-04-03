import mimetypes
import os
import smtplib
import ssl

from email.message import EmailMessage
from dotenv import load_dotenv

# Trying to import email_content
try:
    import email_content
except ImportError:
    raise RuntimeError("The email_content.py file is missing.")

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

def create_plain_message(receivers, sender, subject, body):
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

def attach_files(msg, files):
    """
    Attach file(s) to the EmailMessage object.

    :param msg: EmailMessage object
    :param files: List of file(s) to be attached
    :return: EmailMessage object with attachment(s)
    """
    for filename in files:
        if not os.path.isfile(filename):
            print(f"The file '{filename}' was not found.")
            continue
        # Guess the content type based on the file's extension. Encoding will be ignored.
        ctype, encoding = mimetypes.guess_file_type(filename)
        if ctype is None or encoding is not None:
            # No guess could be made, or the file is encoded (compressed).
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        with open(filename, 'rb') as fp:
            msg.add_attachment(fp.read(),
                               maintype=maintype,
                               subtype=subtype,
                               filename=os.path.basename(filename))

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
    email_subject, email_body = email_content.subject, email_content.body
    msg = create_plain_message(creds['receivers'], creds['sender'], email_subject, email_body)
    if hasattr(email_content, "files") and email_content.files:
        msg = attach_files(msg, email_content.files)

    send_message("smtp.gmail.com", 465, creds['sender'], creds['password'], creds['receivers'], msg, creds['bcc'])

if __name__ == "__main__":
    main()