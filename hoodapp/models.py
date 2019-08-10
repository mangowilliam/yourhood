from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hood(models.Model):
    image = models.ImageField(default = 'default.jpg',upload_to='images/')
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    count = models.IntegerField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE) 
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering =['pub_date']
    
    def save_hood(self):
        self.save()
    
    def delete_hood(self):
        self.delete()
        
    @classmethod
    def get_hoods(cls):
        hoods = cls.objects.all()
        return hoods
class Profile(models.Model):
    image = models.ImageField(default = 'default.jpg',upload_to='images/')
    bio = models.CharField(max_length=150)
    email = models.EmailField()
    hood = models.ForeignKey(Hood,related_name='hood')
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, related_name='profile') 
    
    def __str__(self):
            return self.user.username

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
class Business(models.Model):
    image = models.ImageField(default = 'default.jpg',upload_to='images/')
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User)
    hood = models.ForeignKey(Hood)
    email = models.EmailField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering =['pub_date']
    
    def save_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()    
    
    @classmethod
    def filter_by_hood(cls,hood_name):
        business = Business.objects.filter(hood=hood_name)
        return business
    @classmethod
    def search_business(cls, names):
        business = cls.objects.filter(hood__name__icontains=names)
        return business
class Post(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 300)
    hood = models.ForeignKey(Hood)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    
    def __str__(self):
        return self.title   
    
    class Meta:
        ordering =['pub_date']
    
    def save_post(self):
        self.save()
    
    def delete_post(self):
        self.delete()
    
    @classmethod
    def filter_by_hood(cls,hood_name):
        posts = Post.objects.filter(hood=hood_name)
        return posts