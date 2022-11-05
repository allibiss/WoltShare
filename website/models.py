from django.db import models


class User(models.Model):
    email = models.CharField("Email", max_length=256)
    password = models.CharField("Password", max_length=256)
    name = models.CharField("Name Surname", max_length=256)
    phone = models.CharField("Phone number", max_length=256, blank=True)
    address = models.CharField("Address", max_length=256)
