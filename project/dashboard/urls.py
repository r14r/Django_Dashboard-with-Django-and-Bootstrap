from django.contrib import admin
from django.urls import include, path

from .settings import CUSTOM_APPS

from apps.pages.dashboard.views import  IndexView as DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='index',),
    path('admin/',  admin.site.urls),
]

for custom_app in CUSTOM_APPS:
    pattern = custom_app.replace('apps.', '')
    urlpatterns.append(
        path(pattern, include(custom_app + '.urls', namespace=custom_app), name=pattern, ),
    )
    
print(f"DEBUG: urls.py | {urlpatterns=}")