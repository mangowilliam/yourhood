from django.shortcuts import render,redirect
from . forms import UserRegistrationForm,userForm,hoodForm,businessForm,profileForm,postForm
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Hood,Business,Post,Profile
# Create your views here.
def hood(request):
   
    hoods = Hood.get_hoods()
    return render(request, "hood.html",{"hoods":hoods})
    
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form =UserRegistrationForm()
    return render(request,'registration/registration_form.html',{'form':form}) 


@login_required(login_url='/accounts/login/')
def add_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = hoodForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('hood')
    else:
        form = hoodForm()
    return render(request, 'newhood.html',{"form": form})
@login_required(login_url='/accounts/login/')
def add_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('hood')
    else:
        form = postForm()
    return render(request, 'newpost.html',{"form": form})
@login_required(login_url='/accounts/login/')
def add_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = businessForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('hood')
    else:
        form = businessForm()
    return render(request, 'newbusiness.html',{"form": form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    id = current_user.id
    hood = current_user.profile.hood
    business = Business.filter_by_hood(hood)
    return render(request, "profile/profile.html",{"business":business})

@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES)
        if form.is_valid():
            myprofile = form.save(commit=False)
            myprofile.username = current_user
            myprofile.save()
            return redirect('profile')
    else:
        form = profileForm()
    return render(request, 'profile/profile-up.html', {"form": form})
@login_required(login_url='/accounts/login/')
def user_update(request):
    if request.method == 'POST':
        form = userForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = userForm(instance=request.user)
    return render(request, "profile/user-up.html", {"form": form})