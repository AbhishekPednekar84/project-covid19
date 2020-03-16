import os
import dotenv
from django.shortcuts import render

dotenv.load_dotenv()


def home(request):
    return render(
        request,
        "covid19_home/home.html",
        {"google_analytics": os.getenv("GOOGLE_ANALYTICS_ID")},
    )
