from django.shortcuts import render

from app.currency.models import Rate, ContactUs, Source
from app.currency.forms import RateForm, MessageForms, SourceForm

from django.http.response import HttpResponseRedirect
from django.http import HttpResponseForbidden

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView

from django.urls import reverse, reverse_lazy

from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.conf import settings


class RateListView(LoginRequiredMixin, ListView):
    queryset = Rate.objects.all().select_related('source')
    template_name = 'rate_list.html'

    def get_object(self, queryset=None):
        qs = self.get_queryset()
        return qs.get(id=self.request.user.id)


class RateCreateView(CreateView):
    model = Rate
    form_class = RateForm
    success_url = reverse_lazy('rate_list')
    template_name = 'rate_create.html'


class RateUpdateView(UserPassesTestMixin, UpdateView):
    model = Rate
    form_class = RateForm
    success_url = reverse_lazy('rate_list')
    template_name = 'rate_update.html'

    def test_func(self):
        return self.request.user.is_superuser

    def hanlde_no_permission(self):
        return HttpResponseForbidden('You can`t change rate')


class RateDeleteView(UserPassesTestMixin, DeleteView):
    model = Rate
    success_url = reverse_lazy('rate_list')
    template_name = 'rate_delete.html'

    def test_func(self):
        return self.request.user.is_superuser

    def hanlde_no_permission(self):
        return HttpResponseForbidden('You can`t delete rate')


class RateDetailView(DetailView):
    model = Rate
    template_name = 'rate_details.html'


# --------------------------------------------------------


class MessageListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'message.html'


class MessageCreateView(CreateView):
    form_class = MessageForms
    success_url = reverse_lazy('message-list')
    template_name = 'message_create.html'

    def _send_email(self):
        recipient = settings.DEFAULT_FROM_EMAIL,
        subject = 'User contact us',
        message = f"""
                    Name: {self.object.name}
                    Email: {self.object.email}
                    Subject: {self.object.subject}
                    Message: {self.object.message}
        """
        send_mail(
            subject,
            message,
            recipient,
            [recipient],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_email()
        return redirect


class MessageUpdateView(UpdateView):
    model = ContactUs
    form_class = MessageForms
    success_url = reverse_lazy('message-list')
    template_name = 'message_update.html'


class MessageDeleteView(DeleteView):
    model = ContactUs
    success_url = reverse_lazy('message-list')
    template_name = 'message_delete.html'


class MessageDetailView(DetailView):
    model = ContactUs
    template_name = 'message_detail.html'


# --------------------------------------------------------

class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    success_url = reverse_lazy('source-list')
    template_name = 'source_create.html'


class SourceUpdateView(UpdateView):
    model = Source
    form_class = SourceForm
    success_url = reverse_lazy('source-list')
    template_name = 'source_update.html'


class SourceDeleteView(DeleteView):
    model = Source
    success_url = reverse_lazy('source-list')
    template_name = 'source_delete.html'


class SourceDetailView(DetailView):
    model = Source
    template_name = 'source_details.html'


# --------------------------------------------------------


class IndexView(TemplateView):
    template_name = 'index.html'


def tets_templates(request):
    name = request.GET.get('name')
    context = {
        'username': name
    }

    return render(request, 'test.html', context)


# --------------------------------------------------------

#
# class ProfileView(LoginRequiredMixin, UpdateView):
#     model = get_user_model()
#     template_name = 'registration/profile.html'
#     success_url = reverse_lazy('Index')
#     fields = (
#         'first_name',
#         'last_name',
#     )
#
#     def get_object(self, queryset=None):
#         qs = self.get_queryset()
#         return qs.get(id=self.request.user.id)
