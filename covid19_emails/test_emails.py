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

    def test_send_email_with_invalid_email_address(self):
        request = RequestFactory().post(
            self.path,
            data={
                "from_name": "John Doe",
                "from_email": "JD.com",
                "category": "1",
                "link": "test link",
                "message": "test message",
            },
        )
        response = contact(request)
        assert b"Enter a valid email address." in response.content
