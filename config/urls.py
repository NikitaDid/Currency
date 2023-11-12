
from django.contrib import admin
from django.urls import path
from app.currency.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/world', hello)
]
