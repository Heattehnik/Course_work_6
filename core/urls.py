from django.urls import path
from core.apps import CoreConfig
from core.views import contacts

app_name = CoreConfig.name

urlpatterns = [
    path('', contacts, name='contacts'),
]