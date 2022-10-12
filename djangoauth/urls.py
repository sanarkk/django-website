from django.urls import path
from .views import index, Home

urlpatterns = [
    path('', Home.as_view(), name="home"),
]