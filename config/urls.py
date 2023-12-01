from django.contrib import admin
from django.urls import path
from app.currency.views import (
    rate_list,
    rate_create,
    rate_update,
    rate_delete,
    rate_details,
    message,
    message_create,
    message_update,
    message_delete,
    message_details,
    tets_templates,
    source_list,
    source_create,
    source_update,
    source_delete,
    source_details,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list/', rate_list),
    path('rate/create/', rate_create),
    path('rate/update/<int:pk>/', rate_update),
    path('rate/delete/<int:pk>/', rate_delete),
    path('rate/details/<int:pk>/', rate_details),
    path('contactus/list', message),
    path('message/create', message_create),
    path('message/update/<int:pk>/', message_update),
    path('message/delete/<int:pk>/', message_delete),
    path('message/detail/<int:pk>/', message_details),
    path('source/list', source_list),
    path('source/create/', source_create),
    path('source/update/<int:pk>/', source_update),
    path('source/delete/<int:pk>/', source_delete),
    path('source/details/<int:pk>/', source_details),
    path('template/', tets_templates),
]
