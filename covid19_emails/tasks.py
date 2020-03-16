import os
import dotenv
from celery import shared_task
from django.core.mail import send_mail

dotenv.load_dotenv()


@shared_task
def send_email_task(subject, message, to_email):
    send_mail(
        subject=subject,
        message=message,
        from_email=os.getenv("DEFAULT_FROM_EMAIL"),
        recipient_list=[to_email],
        fail_silently=False,
    )
    return None
