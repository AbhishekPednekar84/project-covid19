from django.db import models


class Fact(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.TextField(max_length=10000)

    def __str__(self):
        return f"{self.question}"


class Myth(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.TextField(max_length=10000)

    def __str__(self):
        return f"{self.question}"


class Prevention(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.TextField(max_length=10000)

    def __str__(self):
        return f"{self.question}"
