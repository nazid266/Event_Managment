from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_image',blank=True,default='profile_image/default_img.jpeg')
    phone = PhoneNumberField(unique=True,blank=True,null=True,region='BD')
    bio=models.TextField(blank=True)

    def __str__(self):
        return self.username
