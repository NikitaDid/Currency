from django.db import models
from django.utils.translation import gettext_lazy as _
from app.currency.choices import (
    CurrencyTypeChoices,
    SOURCE_TYPE,
    SOURCE_URL_TYPE,
    CURRENCY_PRIVAT,
)
from django.contrib.auth.models import AbstractUser


class Rate(models.Model):
    buy = models.DecimalField(_('Buy'), max_digits=5, decimal_places=2)
    sell = models.DecimalField(_('Sell'), max_digits=5, decimal_places=2)
    created = models.DateTimeField(_('Created'), auto_now_add=True)  # usd, euro, etc
    change_type = models.SmallIntegerField(
        _('Change Type'),
        choices=CurrencyTypeChoices.choices,
        default=CurrencyTypeChoices.USD,
    )
    source = models.CharField(_('Source'), max_length=255, choices=SOURCE_TYPE, default=CURRENCY_PRIVAT)

    class Meta:
        verbose_name = _('Rate')
        verbose_name_plural = _('Rates')

    def __str__(self):
        return f'{self.buy} - {self.sell} - {self.source}'


class ContactUs(models.Model):
    name = models.CharField(_('Name'), max_length=64, default='nikita')
    email = models.EmailField(_('Email'), max_length=254, default='nikitaaa@gmail.com')
    subject = models.CharField(_('Subject'), max_length=254)
    message = models.CharField(_('Message'), max_length=254)

    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE, related_name='rates')

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')


class Source(models.Model):
    source_url = models.URLField(
        _('Source url'),
        max_length=255,
        choices=SOURCE_URL_TYPE,
    )

    source_name = models.CharField(
        _('Source name'),
        max_length=64,
        choices=SOURCE_TYPE,
        default=CURRENCY_PRIVAT,
    )
    created = models.DateTimeField(_('Created'), auto_now_add=True)

    logo = models.FileField(
        _('Logo'),
        default=None,
        null=True,
        blank=True,
        upload_to='static/'
    )

    class Meta:
        verbose_name = _('Source')
        verbose_name_plural = _('Sources')


class RequestResponseLog(models.Model):
    path = models.CharField(
        _('Path'),
        max_length=256,
    )
    request_method = models.CharField(
        _('Request_method'),
        max_length=256,
    )
    time = models.FloatField(
        _('Time'),
    )
