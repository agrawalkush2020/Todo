from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import UserRegistrationForm, UserLoginForm

# Create your views here.

def signup(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request,'tasks/index.html')
        form = UserRegistrationForm()
        return render(request,'users/signup.html',{'form':form})
    elif request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            user = User(username=username, email=email)
            user.set_password(password)
            user.save()

            login_form = UserLoginForm()
            return render(request,'users/login.html',{'form':login_form})
        else:
            return render(request,'users/signup.html',{'form':form})

def login(request):
    if request.method=='GET':
        if request.user.is_authenticated()
            return render(request, 'tasks/index.html')
        else:
            form = UserLoginForm()
            return render(request,'users/login.html',{'form':form})
    else:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # yhn login and authenticate functions use honge, and




