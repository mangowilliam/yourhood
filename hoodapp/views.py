from django.shortcuts import render,redirect
from . forms import UserRegistrationForm,userForm,newHoodForm,businessForm,profileForm,postForm,hoodForm
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Hood,Business,Post,Profile
from .email import send_welcome_email
# Create your views here.
def hood(request):
   
    hoods = Hood.get_hoods()
    return render(request, "hood.html",{"hoods":hoods})
    
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
           # username = form.cleaned_data.get('username') 
           # email = form.cleaned_data['email']
           # send_welcome_email(username,email)
            return redirect('/accounts/login')
    else:
        form =UserRegistrationForm()
    return render(request,'registration/registration_form.html',{'form':form}) 


@login_required(login_url='/accounts/login/')
def add_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = newHoodForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('hood')
    else:
        form = newHoodForm()
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
        return redirect('hood.html')
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
        return redirect('hood.html')
    else:
        form = businessForm()
    return render(request, 'newbusiness.html',{"form": form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    id = current_user.id
    hood = current_user.profile.hood
    business = Business.filter_by_hood(hood)
    posts = Post.filter_by_hood(hood)
    return render(request, "profile/profile.html",{"business":business, "posts":posts})

@login_required(login_url='/accounts/login/')
def add_profile(request):
    try:
        current_user = request.user
    except DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES)
        if form.is_valid():
            myprofile = form.save(commit=False)
            myprofile.username = current_user
            myprofile.save()
            return redirect('details')
    else:
        form = profileForm()
    return render(request, 'profile/profile-up.html', {"form": form})

@login_required(login_url='/accounts/login/')
def hood_update(request):
    if request.method == "POST":
        u_form = userForm(request.POST, instance=request.user)
        p_form = hoodForm(request.POST,request.FILES,  instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = userForm(instance=request.user)
        p_form = hoodForm(instance=request.user.profile.hood)
    twoforms ={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'profile/hoodup.html',twoforms)
@login_required(login_url='/accounts/login/')
def search_business(request):
    
    if 'business' in request.GET and request.GET["business"]:
        names = request.GET.get("business")
        hoodbusinesses = Business.search_business(names)
        print(hoodbusinesses)
        message = f"{names}"

        return render(request, 'search.html', {"message": message, "businesses": hoodbusinesses})

    else:
        message = "You haven't searched for any hood"
        return render(request, 'search.html', {"message": message})