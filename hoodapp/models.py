from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    image = models.ImageField(default = 'default.jpg',upload_to='images/')
    bio = models.CharField(max_length=150)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, related_name='profile') 
    
    def __str__(self):
            return self.user.username

        
class Hood(models.Model):
    image = models.ImageField(default = 'default.jpg',upload_to='images/')
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    count = models.IntegerField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE) 
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Business(models.Model):
    image = models.ImageField(default = 'default.jpg',upload_to='images/')
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User)
    hood = models.ForeignKey(Hood)
    email = models.EmailField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
class Post(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 300)
    pub_date = models.DateTimeField(auto_now_add=True)
