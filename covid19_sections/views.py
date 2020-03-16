import os
import dotenv
from django.shortcuts import render
from .models import Fact, Myth, Prevention

dotenv.load_dotenv()


def facts(request):

    context = {
        "details": Fact.objects.all(),
        "title": "Facts",
        "message": "facts",
        "heading": "COVID-19 - The Facts",
        "source": "The World Health Organization (WHO)",
        "google_analytics": os.getenv("GOOGLE_ANALYTICS_ID"),
    }
    return render(request, "covid19_sections/section.html", context=context)


def myths(request):
    context = {
        "details": Myth.objects.all(),
        "title": "Myths",
        "message": "myths",
        "heading": "COVID-19 - Debunk the Myths!",
        "source": "The World Health Organization (WHO), CDC",
        "google_analytics": os.getenv("GOOGLE_ANALYTICS_ID"),
    }
    return render(request, "covid19_sections/section.html", context=context)


def prevention(request):
    context = {
        "details": Prevention.objects.all(),
        "title": "Prevention Measures",
        "message": "prevention measures",
        "heading": "COVID-19 - Prevention Measures",
        "source": "The World Health Organization (WHO)",
        "google_analytics": os.getenv("GOOGLE_ANALYTICS_ID"),
    }
    return render(request, "covid19_sections/section.html", context=context)


def information(request):
    context = {
        "title": "Information",
        "heading": "Useful Information",
        "google_analytics": os.getenv("GOOGLE_ANALYTICS_ID"),
    }
    return render(request, "covid19_sections/information.html", context=context)
