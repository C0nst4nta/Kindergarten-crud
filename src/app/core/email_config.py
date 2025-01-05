import os

class EmailConfig:
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")  # Example: Gmail SMTP
    SMTP_PORT = os.getenv("SMTP_PORT", 587)  # 587 is the common port for TLS
    SMTP_USER = os.getenv("SMTP_USER")  # Email ID
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")  # Password or app-specific password
    FROM_EMAIL = os.getenv("FROM_EMAIL")  # Same as SMTP_USER
