from .views import get_status
from django.urls import path



urlpatterns = [
    path("", get_status),
]