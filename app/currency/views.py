from django.shortcuts import render
from app.currency.models import Rate, ContactUs, Source
from app.currency.forms import RateForm, MessageForms, SourceForm
from django.http.response import HttpResponseRedirect


def rate_list(request):
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }

    return render(request, 'rate_list.html', context)


def rate_create(request):
    if request.method == 'POST':
        form = RateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    else:
        form = RateForm()
    context = {
        'form': form
    }
    return render(request, 'rate_create.html', context)


def rate_update(request, pk):
    rate = Rate.objects.get(id=pk)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm(instance=rate)
    context = {
        'form': form

    }
    return render(request, 'rate_update.html', context)


def rate_delete(request, pk):
    rate = Rate.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'rate': rate
        }
        return render(request, 'rate_delete.html', context)

    elif request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate/list/')


def rate_details(request, pk):
    rate = Rate.objects.get(id=pk)
    context = {
        'rate': rate
    }
    return render(request, 'rate_details.html', context)


# --------------------------------------------------------

def message(request):
    infos = ContactUs.objects.all()
    context = {
        'infos': infos
    }

    return render(request, 'message.html', context)


def message_create(request):
    if request.method == 'POST':
        form = MessageForms(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contactus/list')
    else:
        form = MessageForms()
        context = {
            'form': form
        }
        return render(request, 'message_create.html', context)


def message_update(request, pk):
    info_ = ContactUs.objects.get(id=pk)

    if request.method == 'POST':
        form = MessageForms(request.POST, instance=info_)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contactus/list')
    elif request.method == 'GET':
        form = MessageForms(instance=info_)
    context = {
        'form': form

    }
    return render(request, 'message_update.html', context)


def message_delete(request, pk):
    info_ = ContactUs.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'info_': info_
        }
        return render(request, 'message_delete.html', context)

    elif request.method == 'POST':
        info_.delete()
        return HttpResponseRedirect('/contactus/list')


def message_details(request, pk):
    info = ContactUs.objects.get(id=pk)
    context = {
        'info': info
    }
    return render(request, 'message_detail.html', context)


# --------------------------------------------------------

def source_list(request):
    banks = Source.objects.all()
    context = {
        'banks': banks
    }
    return render(request, 'source_list.html', context)


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list')
    else:
        form = SourceForm()
    context = {
        'form': form
    }
    return render(request, 'source_create.html', context)


def source_update(request, pk):
    bank = Source.objects.get(id=pk)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=bank)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list')
    elif request.method == 'GET':
        form = SourceForm(instance=bank)
    context = {
        'form': form
    }
    return render(request, 'rate_update.html', context)


def source_delete(request, pk):
    bank = Source.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'bank': bank
        }
        return render(request, 'source_delete.html', context)

    elif request.method == 'POST':
        bank.delete()
        return HttpResponseRedirect('/source/list')


def source_details(request, pk):
    bank = Source.objects.get(id=pk)
    context = {
        'bank': bank
    }
    return render(request, 'source_details.html', context)


# --------------------------------------------------------
def tets_templates(request):
    name = request.GET.get('name')
    context = {
        'username': name
    }

    return render(request, 'test.html', context)
