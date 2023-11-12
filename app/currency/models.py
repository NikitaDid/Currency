from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(..., max_digits=5, decimal_places=2)
    sell = models.DecimalField(..., max_digits=5, decimal_places=2)
    type = models.DateField()  # usd, euro, etc
    created = models.CharField(max_length='3')
