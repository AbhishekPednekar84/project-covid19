from django.urls import reverse, resolve
from django.test import RequestFactory
from .views import home


class HomeTests:
    def test_home_page(self, client):
        path = reverse("covid19-home")
        request = RequestFactory().get(path)
        response = home(request)
        assert response.status_code == 200
        assert b"coronavirus" in response.content
        assert b"COVID-19" in response.content

    def test_home_view(self):
        path = reverse("covid19-home")
        assert resolve(path).view_name == "covid19-home"
