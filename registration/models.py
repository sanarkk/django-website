from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, phone_number, email, password):
        if first_name is None:
            raise TypeError("Users must have a first name.")

        if last_name is None:
            raise TypeError("Users must have a last name.")

        if phone_number is None:
            raise TypeError("Users must have a phone number.")

        if email is None:
            raise TypeError("Users must have a email")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, first_name, last_name, phone_number, email, password):
        if password is None:
            raise TypeError("Users must have a password")

        user = self.create_user(first_name, last_name, phone_number, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(db_index=True, max_length=255, unique=True)
    last_name = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    phone_number = models.CharField(db_index=True, max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number"]

    def __str__(self):
        return f"{self.email}"
