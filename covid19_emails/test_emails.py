from django.urls import resolve, reverse
from django.test import RequestFactory, TestCase
from .views import contact


class ContactTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ContactTests, cls).setUpClass()
        cls.path = reverse("covid19-contact")

    def test_contact_page(self):
        request = RequestFactory().get(self.path)
        response = contact(request)
        assert response.status_code == 200
        assert b"Contact Us" in response.content

    def test_contact_view(self):
        assert resolve(self.path).view_name == "covid19-contact"
