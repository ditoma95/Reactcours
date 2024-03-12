from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50,blank=True,null=True)
    phone = models.CharField(max_length=100, unique=True)
    notes = models.CharField(max_length=500,blank=True,null=True)
    avatar = models.ImageField(null=True,default=None,blank=True)
    stared = models.BooleanField()