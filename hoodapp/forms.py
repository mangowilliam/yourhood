from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Hood,Profile,Business,Post

class UserRegistrationForm(UserCreationForm):
    email =forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class hoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        exclude = ['pub_date']
class postForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['pub_date']
class businessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['pub_date']

class userForm(forms.ModelForm):
    email =forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email',]

class hoodForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['hood']


class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username',]