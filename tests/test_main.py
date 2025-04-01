import pytest

from email.message import EmailMessage
from main import create_message

def test_create_message():
    sender = "from@example.com"
    receivers = ["to@example.com"]
    subject = "Hello"
    body = "This is a test"

    msg = create_message(receivers, sender, subject, body)

    assert isinstance(msg, EmailMessage)
    assert msg["From"] == sender
    assert msg["To"] == "to@example.com"
    assert msg["Subject"] == subject
    assert msg.get_content().strip() == body
