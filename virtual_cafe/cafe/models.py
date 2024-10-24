from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    coffee_status = models.BooleanField(default=False)
    is_present = models.BooleanField(default=False)
