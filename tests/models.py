from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255)
    line3 = models.CharField(max_length=255)

    raw_data = models.TextField()
