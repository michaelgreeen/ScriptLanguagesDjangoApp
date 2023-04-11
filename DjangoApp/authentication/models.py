from django.db import models

# Create your models here.
from hashlib import new
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(blank = False, unique=True, max_length = 255)
    password = models.CharField(blank = True, max_length = 255)
    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username