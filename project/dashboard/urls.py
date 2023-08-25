from django.contrib import admin
from django.urls import path

import apps.frontend.views as views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
]
