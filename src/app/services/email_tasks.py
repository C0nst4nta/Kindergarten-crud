from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import logging
from celery import Celery

# Set up logging
logging.basicConfig(level=logging.INFO)

# Celery app instance
celery_app = Celery(
    'tasks',
    result_backend='redis://redis-container:6379/0',  # Use Docker DNS for Redis
    broker='redis://redis-container:6379/0'  # Use Docker DNS for Redis
)

# Celery configuration settings (optional)
celery_app.conf.update(
    result_expires=3600,
    task_serializer='json',
    broker_connection_retry_on_startup=True
)

# Email configuration
class EmailConfig:
    FROM_EMAIL = "magzhanzeinolla13@gmail.com"
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USER = "magzhanzeinolla13@gmail.com"
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")  # Use environment variables for production!

@celery_app.task(bind=True, max_retries=3, default_retry_delay=30)
def send_email(self, subject: str, body: str, to_email: str):
    """Send email asynchronously using smtplib and Celery."""
    msg = MIMEMultipart()
    msg["From"] = EmailConfig.FROM_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(EmailConfig.SMTP_SERVER, EmailConfig.SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(EmailConfig.SMTP_USER, EmailConfig.SMTP_PASSWORD)
            server.sendmail(EmailConfig.FROM_EMAIL, to_email, msg.as_string())
        logging.info(f"Email sent to {to_email}")
    except Exception as e:
        logging.error(f"Failed to send email: {str(e)}")
        raise self.retry(exc=e)  # Retry the task if it fails
