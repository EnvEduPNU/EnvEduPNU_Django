from django.urls import include, path
from .views import main

app_name = 'main'

urlpatterns = [
    path('main', main.as_view(), name='main'),
]