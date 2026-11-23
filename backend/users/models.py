# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import BaseModel


class CustomUser(AbstractUser, BaseModel):
    """Application user authenticated with an email address."""

    email = models.EmailField(unique=True)
    address = models.TextField(null=True,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
