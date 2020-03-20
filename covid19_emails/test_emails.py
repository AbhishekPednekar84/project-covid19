from django.urls import resolve, reverse
from django.test import RequestFactory, TestCase
from .views import contact
from .forms import ContactForm


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

    def test_contact_form_with_valid_data(self):
        form = ContactForm(
            data={
                "from_name": "John Doe",
                "from_email": "jd@email.com",
                "category": "1",
                "link": "Some source",
                "message": "Test Message",
            }
        )
        assert form.is_valid()

    def test_contact_form_with_no_data(self):
        form = ContactForm(data={})
        assert not (form.is_valid())
        assert len(form.errors) == 5

    def test_contact_form_with_invalid_email(self):
        form = ContactForm(
            data={
                "from_name": "John Doe",
                "from_email": "jd.com",
                "category": "1",
                "link": "Some source",
                "message": "Test Message",
            }
        )
        assert not (form.is_valid())
        assert len(form.errors) == 1
