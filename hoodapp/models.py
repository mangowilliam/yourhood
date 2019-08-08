from django.db import models


# Create your models here.
class UserS(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
  
    def __str__(self):
            return self.name