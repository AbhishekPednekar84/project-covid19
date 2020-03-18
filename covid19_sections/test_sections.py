import pytest
from django.urls import reverse, resolve
from django.test import RequestFactory, TestCase
from .views import facts, myths, prevention, information, helplines
from .models import Fact, Myth, Prevention
from mixer.backend.django import mixer


@pytest.mark.django_db
class FactsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(FactsTests, cls).setUpClass()
        cls.path = reverse("covid19-section-facts")

    def test_facts_page(self):
        request = RequestFactory().get(self.path)
        response = facts(request)
        assert response.status_code == 200

    def test_facts_model(self):
        fact = mixer.blend(Fact, question="What is COVID-19?")
        assert fact.question == "What is COVID-19?"

    def test_facts_view(self):
        assert resolve(self.path).view_name == "covid19-section-facts"


@pytest.mark.django_db
class MythsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(MythsTests, cls).setUpClass()
        cls.path = reverse("covid19-section-myths")

    def test_myths_page(self):
        request = RequestFactory().get(self.path)
        response = myths(request)
        assert response.status_code == 200

    def test_myths_model(self):
        myth = mixer.blend(
            Myth, question="Cold weather and snow can kill the new coronavirus."
        )
        assert (
            myth.question
            == "Cold weather and snow can kill the new coronavirus."
        )

    def test_myths_view(self):
        assert resolve(self.path).view_name == "covid19-section-myths"


@pytest.mark.django_db
class PreventionTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(PreventionTests, cls).setUpClass()
        cls.path = reverse("covid19-section-prevention")

    def test_prevention_page(self):
        request = RequestFactory().get(self.path)
        response = prevention(request)
        assert response.status_code == 200

    def test_prevention_model(self):
        prevention = mixer.blend(
            Prevention, question="Wash your hands frequently"
        )
        assert prevention.question == "Wash your hands frequently"

    def test_prevention_view(self):
        assert resolve(self.path).view_name == "covid19-section-prevention"


class InformationTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(InformationTests, cls).setUpClass()
        cls.path = reverse("covid19-section-information")

    def test_information_page(self):
        request = RequestFactory().get(self.path)
        response = information(request)
        assert response.status_code == 200

    def test_information_view(self):
        assert resolve(self.path).view_name == "covid19-section-information"


@pytest.mark.django_db
class HelplineTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(HelplineTests, cls).setUpClass()
        cls.path = reverse(
            "covid19-section-helplines", kwargs={"country": "india"}
        )

    def test_helpline_page(self):
        request = RequestFactory().get(self.path)
        response = helplines(request, country="india")
        assert response.status_code == 200

    def test_helpline_view(self):
        assert resolve(self.path).view_name == "covid19-section-helplines"
