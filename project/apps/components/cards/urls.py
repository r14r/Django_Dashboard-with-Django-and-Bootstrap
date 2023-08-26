from django.urls import path

from . import apps
from . import views

app_name = 'apps.components.cards'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index',),
]
