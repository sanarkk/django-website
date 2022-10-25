from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from core.settings.base import LANGUAGES, LANGUAGE_CODE


# Create your models here.




class UserProfile(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    phone_number = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed.",
            ),
        ],
    )

    language = models.CharField(
        choices=LANGUAGES, default=LANGUAGE_CODE, max_length=10
    )

    objects = models.Manager()

    def __str__(self):
        return f"{self.user.username}"
