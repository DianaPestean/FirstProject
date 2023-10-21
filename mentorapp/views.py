from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import  LoginView
from django.contrib.auth.decorators import login_required




# Create your views here.


def home(request):
    users_context = {}
    return render(request, template_name="base.html", context=users_context)

def user_login(request):
    if request.method == "GET":
        form = LogInForm()
        return render(request,template_name="mentorapp/login.html",context={"form":form})
    elif request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            user_password = form.cleaned_data["user_password"]
            user = authenticate(request, username = user_name, password = user_password)
            if user:
                login(request,user)
                messages.success(request,"Ai fost autentificat !")
                return redirect('home')
        messages.error(request,"Autentificare nereusita !")
        return render(request,template_name="mentorapp/login.html",context={"form":form})


def user_signup(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request,template_name="mentorapp/signup.html",context={"form":form})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # user_name = form.cleaned_data["user_name"]
            # user_password = form.cleaned_data["password"]
            user = form.save()
            return redirect('home')
        else:
            print("Forma invalida")
            print(form.errors)


def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out !")
    return redirect("sign-in")
