from django.contrib import admin
from . models import Profile,Business,Hood,User

# Register your models here.
admin.site.register(User)
admin.site.register(Business)
admin.site.register(Hood)
admin.site.register(Profile)