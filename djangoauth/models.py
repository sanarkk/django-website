from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    phone_number = models.CharField(max_length=15)

    objects = models.Manager()

    def __str__(self):
        return f"{self.first_name} | {self.last_name}"
