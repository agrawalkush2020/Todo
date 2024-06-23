from django.contrib.auth import authenticate, login as Login, logout as Logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages
# Create your views here.


@csrf_exempt
def signup(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')
        form = UserRegistrationForm()
        return render(request, 'users/signup.html', {'form': form})
    elif request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            user = User(username=username, password=password)
            user.set_password(password)  #hashkrke passwrod set kiya
            user.save()

            return redirect('login')
        else:
            return render(request, 'users/signup.html', {'form': form})


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')
        else:
            form = UserLoginForm()
            return render(request, 'users/login.html', {'form': form})
    else:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user:  # User object
                Login(request, user=user)
                return redirect('index')
            else:
                #message likhke isliye bhjre hain jisse puraane credentials bhi dikhe and message bhi ajaaye
                #dobaara render ni kiya poora nya form, jisse ussi mein changes kr paaye banda
                messages.error(request, "Invalid username or password")
                return render(request, 'users/login.html', {'form': form})
                # redirect('login')

            # yhn login and authenticate functions use honge, and


@login_required
def logout(request):
    if request.user.is_authenticated: #True/False
        Logout(request)
    return redirect('login')
