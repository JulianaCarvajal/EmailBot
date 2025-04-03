import pytest

from email.message import EmailMessage
from main import attach_files, create_plain_message

def test_create_plain_message():
    sender = "from@example.com"
    receivers = ["to@example.com"]
    subject = "Hello"
    body = "This is a test"

    msg = create_plain_message(receivers, sender, subject, body)

    assert isinstance(msg, EmailMessage)
    assert msg["From"] == sender
    assert msg["To"] == "to@example.com"
    assert msg["Subject"] == subject
    assert msg.get_content().strip() == body

def test_attach_files_add_attachment(tmp_path):
    file_path = tmp_path / "hello.txt"
    file_path.write_text("test content", encoding="utf-8")

    msg = EmailMessage()
    files = [str(file_path)]

    msg = attach_files(msg, files)

    attachment_list = list(msg.iter_attachments())

    assert len(attachment_list) == 1
    assert  attachment_list[0].get_filename() == "hello.txt"

def test_attach_files_missing_files():
    msg = EmailMessage()
    files = ["Nonexistent_file.txt"]
    msg = attach_files(msg, files)

    assert list(msg.iter_attachments()) == []