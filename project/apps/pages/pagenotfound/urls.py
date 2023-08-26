from django.urls import path

from . import apps
from . import views

app_name = apps.PagenotfoundConfig.name

urlpatterns = [
    path('', views.IndexView.as_view(), name='index',),
]
