from django.contrib import admin
from django.urls import include, path

from .settings import CUSTOM_APPS

from apps.pages.main.views import  index

urlpatterns = [
    path('', index, name='index',),
    path('admin/',  admin.site.urls),
]

for custom_app in CUSTOM_APPS:
    pattern = custom_app.replace('apps.', '')
    urlpatterns.append(
        path(pattern, include(custom_app + '.urls', namespace=custom_app), name=pattern, ),
    )
