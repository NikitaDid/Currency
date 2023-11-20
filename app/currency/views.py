from django.shortcuts import render
from app.currency.models import Rate, ContactUs


def rate_list(request):
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }

    return render(request, 'rate_list.html', context)


def message(request):
    infos = ContactUs.objects.all()
    context = {
        'infos': infos
    }

    return render(request, 'message.html', context)


def tets_templates(request):
    name = request.GET.get('name')
    context = {
        'username': name
    }

    return render(request, 'test.html', context)
