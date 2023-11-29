from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    sell = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)  # usd, euro, etc
    change_type = models.CharField(max_length=3)
    source = models.CharField(max_length=255)


class ContactUs(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.TextField(verbose_name='subject')
    message = models.TextField(verbose_name='message')


class Source(models.Model):
    source_url = models.URLField(max_length=255)
    source_name = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)