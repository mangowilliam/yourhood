from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Hood(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    count = models.IntegerField()
    admin = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    
    
class Business(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User)
    hood = models.ForeignKey(Hood)
    email = models.EmailField()

class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    id = models.ForeignKey(User, primary_key=True uni)
    hood = models.ForeignKey(Hood, null=True, blank=True)
    
    def __str__(self):
            return self.name
class Profile(models.Model):
    image = models.ImageField(default = 'default.jpg',upload_to='images/')
    bio = models.CharField(max_length=150)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, related_name='profile') 
    
    
    def __str__(self):
            return self.user.username
    class Meta:
        ordering =['bio']
    
    def save_profile(self):
        self.save()
    def update_profile(self):
        self.update()
    def delete_profile(self):
        self.delete()
