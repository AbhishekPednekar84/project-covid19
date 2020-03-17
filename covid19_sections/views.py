import os
import dotenv
from django.shortcuts import render
from .models import Fact, Myth, Prevention, Helpline, Country

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


def helplines(request, country):

    country_data = Country.objects.filter(country__iexact=country).first()

    if country_data:
        country_name = country_data.country
        national_helpline_number = country_data.national_helpline
        national_helpline_email = country_data.national_email
        source = country_data.information_source

        context = {
            "country": country_name,
            "title": country_name,
            "national_helpline": national_helpline_number,
            "national_email": national_helpline_email,
            "source": source,
            "details": Helpline.objects.filter(
                country_id=country_data.id
            ).order_by("state"),
        }

        return render(
            request, "covid19_sections/helplines.html", context=context
        )
    return render(request, "covid19_sections/404.html")
