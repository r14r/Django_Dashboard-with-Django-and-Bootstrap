from django.urls import path

from . import apps
from . import views

app_name = 'pages.charts'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index',),
]


print(f"DEBUG: app_name={app_name}")