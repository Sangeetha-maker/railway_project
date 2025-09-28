from django.urls import path
from .views import TrainList

urlpatterns = [
    path('trains/', TrainList.as_view()),
]