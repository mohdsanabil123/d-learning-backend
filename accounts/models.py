from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Custom User Model

class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    school_name = models.CharField(max_length=100, null=True, blank=True)
    std = models.CharField(max_length=50, null=True, blank=True)
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']
    
    objects = UserManager()