import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.celery_config import celery_app
from app.core.email_config import EmailConfig


@celery_app.task
def send_email(subject: str, body: str, to_email: str):
    """Send email asynchronously using smtplib and Celery."""
    # Setting up the email parameters
    msg = MIMEMultipart()
    msg['From'] = EmailConfig.FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(EmailConfig.SMTP_SERVER, EmailConfig.SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(EmailConfig.SMTP_USER, EmailConfig.SMTP_PASSWORD)
            server.sendmail(EmailConfig.FROM_EMAIL, to_email, msg.as_string())
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
