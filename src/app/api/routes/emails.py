from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.email_tasks import send_email

router = APIRouter()

class EmailRequest(BaseModel):
    subject: str
    body: str
    to_email: str

@router.post("/send-email/")
async def send_email_endpoint(email_request: EmailRequest):
    """Trigger Celery task to send email."""
    try:
        # Call Celery task asynchronously
        send_email.apply_async(args=[email_request.subject, email_request.body, email_request.to_email])
        return {"message": f"Email sending to {email_request.to_email} is in progress."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
