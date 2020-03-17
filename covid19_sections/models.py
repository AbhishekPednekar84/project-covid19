from django.db import models


class Fact(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.TextField(max_length=10000)

    def __str__(self):  # pragma: no cover
        return f"{self.question}"


class Myth(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.TextField(max_length=10000)

    def __str__(self):  # pragma: no cover
        return f"{self.question}"


class Prevention(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.TextField(max_length=10000)

    def __str__(self):  # pragma: no cover
        return f"{self.question}"


class Country(models.Model):
    country = models.CharField(max_length=100)
    national_helpline = models.CharField(max_length=100, blank=True)
    national_email = models.EmailField(blank=True)
    country_abbr = models.CharField(max_length=50)
    information_source = models.CharField(max_length=50, blank=True)

    def __str__(self):  # pragma: no cover
        return f"{self.country}"


class Helpline(models.Model):
    state = models.CharField(max_length=100)
    helpline = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):  # pragma: no cover
        return f"{self.country} - {self.state}"
