import os
import dotenv
from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from .tasks import send_email_task

dotenv.load_dotenv()


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["from_name"]
            email = form.cleaned_data["from_email"]
            category = form.cleaned_data["category"]
            link = form.cleaned_data["link"]
            message = form.cleaned_data["message"]

            # Temporary implementation
            categories = {  # pragma: no cover
                "1": "general information",
                "2": "facts",
                "3": "myths",
                "4": "preventive measures",
            }

            # User submitted data
            subject = f"COVID-19 {categories[category]} submitted"
            message = (
                f"Email from {name} ({email})"
                + "\n\n"
                + message
                + "\n\n"
                + link
            )
            to_email = os.getenv("DEFAULT_TO_EMAIL")

            # Acknowledgement
            ack_subject = f"Thanks for your submission!"  # pragma: no cover
            ack_message = (  # pragma: no cover
                f"Hey {name}," + "\n\n"
                f"We appreciate your contribution to our growing list of COVID-19 {categories[category]}. "
                f"We will review the information based on the source that you provided. "
                f"You will be notified if it is added to the list."
                + "\n\n"
                + "Thanks!"
                + "\n\n"
                f"Please do not respond to this email as the mailbox is not monitored."
            )
            ack_to_email = email  # pragma: no cover

            send_email_task.delay(subject, message, to_email)
            send_email_task.delay(ack_subject, ack_message, ack_to_email)
            messages.success(request, "Thanks! We will be in touch soon.")
    else:
        form = ContactForm()

    return render(
        request,
        "covid19_emails/contact.html",
        {"form": form, "google_analytics": os.getenv("GOOGLE_ANALYTICS_ID")},
    )
