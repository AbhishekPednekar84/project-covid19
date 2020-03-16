from django.urls import path
from . import views

urlpatterns = [
    path("facts/", views.facts, name="covid19-section-facts"),
    path("myths/", views.myths, name="covid19-section-myths"),
    path("prevention/", views.prevention, name="covid19-section-prevention"),
    path("information/", views.information, name="covid19-section-information"),
]
