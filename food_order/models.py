from django.db import models
from dishes_page.models import Dish
from django.contrib.auth.models import User

# Create your models here.
class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    dishes = models.BooleanField(null=True)
    order_date = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.order_date}"