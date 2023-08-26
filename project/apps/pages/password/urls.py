from django.urls import path

from . import apps
from . import views

app_name = apps.PasswordConfig.name

urlpatterns = [
    path('', views.IndexView.as_view(), name='index',),
]
