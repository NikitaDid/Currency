from django.shortcuts import HttpResponse
from app.currency.models import Rate, ContactUs


def rate_list(request):
    results = []
    rates = Rate.objects.all()

    for rate in rates:
        results.append(
            f'ID: {rate.id}, buy: {rate.buy}, sell: {rate.sell}, type:{rate.type},'
            f' source: {rate.source}, created: {rate.created} <br>'
        )

    return HttpResponse(str(results))


def message(request):
    results = []
    infos = ContactUs.objects.all()

    for info in infos:
        results.append(
            f'ID: {info.id}, email: {info.email}, subject: {info.subject}, message:{info.message} <br>'
        )

    return HttpResponse(str(results))
