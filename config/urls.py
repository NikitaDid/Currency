from django.contrib import admin
from django.urls import path, include
from app.currency.views import tets_templates, IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.currency.urls')),
    path('template/', tets_templates),
    path('', IndexView.as_view()),

]
