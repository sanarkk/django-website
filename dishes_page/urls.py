from django.urls import path
from .views import DishesView

urlpatterns = [
    path("", DishesView.as_view(), name="dishes"),
]
