from django.db import models


class CurrencyTypeChoices(models.IntegerChoices):
    USD = 1, 'Dollar_USA'
    EUR = 2, 'Euro_Europe'
    UAH = 3, 'Ukranian_hryvnia'
    PLN = 4, 'Polish_zloty'
    CNY = 5, 'Chinese_Yuan'


CURRENCY_PIVDENNY = 'PIVDENNY'
CURRENCY_PRIVAT = 'PRIVAT'
CURRENCY_CREDITDNEPR = 'CREADITDNEPR'
CURRENCY_MONOBANK = 'MONOBANK'
SOURCE_TYPE = (
    (CURRENCY_PIVDENNY, 'Bank Pivdenny'),
    (CURRENCY_PRIVAT, 'Bank Privat'),
    (CURRENCY_CREDITDNEPR, 'Bank Credir Dnepro'),
    (CURRENCY_MONOBANK, 'Bank Mono'),
)

SOURCE_URL_TYPE = (
    ('https://bank.com.ua/en', 'Bank Pivdenny'),
    ('https://en.privatbank.ua/', 'Bank Privat'),
    ('https://creditdnepr.com.ua/en', 'Bank Credir Dnepro'),
    ('https://www.monobank.ua/?lang=en', 'Bank Mono'),

)
