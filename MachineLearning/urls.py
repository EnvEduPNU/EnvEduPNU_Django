from django.urls import include, path
from .views import MachineLearning

app_name = 'MachineLearning'

urlpatterns = [
    path('learn', MachineLearning.as_view(), name='MachineLearning'),
]