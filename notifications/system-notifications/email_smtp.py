"""SMTP ile sistem e-postası gönderimi."""

from email.mime.text import MIMEText
import smtplib


def send_email(to: str, subject: str, message: str) -> bool:
    """Basit SMTP gönderimi"""
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = "noreply@example.com"
    msg["To"] = to
    try:
        with smtplib.SMTP("localhost") as smtp:
            smtp.send_message(msg)
        return True
    except Exception:
        return False
