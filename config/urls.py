
from django.contrib import admin
from django.urls import path
from app.currency.views import rate_list, message, tets_templates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list', rate_list),
    path('contactus/list', message),
    path('template/', tets_templates),
]

