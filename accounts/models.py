from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.conf import settings

# Custom User Model

class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField( max_length=20, unique=True )
    email = models.EmailField( unique=True )
    address = models.CharField( max_length=200, null=True, blank=True )
    school_name = models.CharField( max_length=100, null=True, blank=True )
    std = models.CharField( max_length=50, null=True, blank=True )
    profile_pic = models.ImageField( upload_to='Profile', blank=True, null=True )
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']
    
    objects = UserManager()

 
# News feed

class News( models.Model ):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='NewsImage')
    
    def __str__(self):
        return self.title
    

class UserAccount( models.Model ):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fee_rate = models.IntegerField(default=500)
    total_amount = models.IntegerField(default=500)
    due_months = models.IntegerField(default=1)
    is_submitted = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user)
    

class Notes( models.Model ):
    subject_name = models.CharField(max_length=100)
    subject_class = models.IntegerField()
    pdf_file = models.FileField(upload_to='PdfNotes')
    
class Contact( models.Model ):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField()