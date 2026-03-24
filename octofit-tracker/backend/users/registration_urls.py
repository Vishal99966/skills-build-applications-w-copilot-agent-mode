from django.urls import path
from .registration import CustomRegisterView

urlpatterns = [
    path('', CustomRegisterView.as_view(), name='rest_register'),
]