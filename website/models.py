from django.db import models


class User(models.Model):
    email = models.CharField("Email", max_length=256)
    password = models.CharField("Password", max_length=256)
    name = models.CharField("Name Surname", max_length=256)
    phone = models.CharField("Phone number", max_length=256, blank=True)
    address = models.CharField("Address", max_length=256)


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE,\
        related_name='%(class)s_seller')
    quantity = models.IntegerField('Quantity')
    price_per_quant = models.FloatField('Price per quantity')
    description = models.CharField('Description', max_length=512)
    type = models.CharField('Type', max_length=256)
    packaging = models.BooleanField('Does it have packaging', default='False')
    # date = models.DateField('Date of posting')
    # expiry_date = models.DateField('Expiry date')


class Transaction(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE,\
        related_name='%(class)s_seller')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE,\
        related_name='%(class)s_buyer')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,\
        related_name='%(class)s_product')
    price = models.IntegerField('Pice')
    quantity = models.IntegerField('Quantity')