from django.shortcuts import render,redirect
from . forms import UserRegistrationForm

# Create your views here.
def hood(request):
    return render(request, "hood.html")
    
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form =UserRegistrationForm()
    return render(request,'registration/registration_form.html',{'form':form}) 