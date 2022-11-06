from django.conf import settings
from django.contrib.auth.models import AbstractUser, User
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)
    username = models.CharField("username", max_length=30, blank=True, unique=True)
    name = models.CharField("Name Surname", max_length=256)
    phone = models.CharField("Phone number", max_length=256, blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    lon = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    # address = models.CharField('address', max_length=256)


FOOD_TYPE_CHOICES = (
    ("PACK", "Packaged"),
    ("INGR", "Ingredient"),
)


class Product(models.Model):
    seller = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="%(class)s_seller"
    )
    quantity = models.IntegerField("Quantity")
    price_per_quant = models.FloatField("Price per quantity")
    description = models.CharField("Description", max_length=512)
    food_type = models.CharField(
        max_length=4, choices=FOOD_TYPE_CHOICES, default="PACK"
    )
    packaging = models.BooleanField("Does it have packaging", default="False")
    # image = models.ImageField('Image', upload_to='products')


class Transaction(models.Model):
    seller = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="%(class)s_seller"
    )
    buyer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="%(class)s_buyer"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="%(class)s_product"
    )
    price = models.IntegerField("Pice")
    quantity = models.IntegerField("Quantity")
