from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    sell = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField()  # usd, euro, etc
    type = models.CharField(max_length=3)
    source = models.CharField(max_length=255)


class ContactUs(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.TextField(verbose_name='subject')
    message = models.TextField(verbose_name='message')
