from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Event(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=200)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    Participants=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="rsvp_events",blank=True)
    asset=models.ImageField( upload_to="event_asset",blank=True,null=True,default="event_asset/default_img.jpeg")
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.name
    


