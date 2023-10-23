from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import  LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def home(request):
    users_context = {}
    return render(request, template_name="base.html", context=users_context)


def user_login_mentor(request):
    if request.method == "GET":
        form = LogInFormMentor()
        return render(request, template_name="mentorapp/login.html", context={"form": form})
    elif request.method == "POST":
        form = LogInFormMentor(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            user_password = form.cleaned_data["user_password"]
            user = authenticate(request, username=user_name, password=user_password)
            if user:
                login(request, user)
                messages.success(request, "Ai fost autentificat !")
                return redirect('home')
        messages.error(request, "Autentificare nereusita !")
        return render(request, template_name="mentorapp/login.html",context={"form":form})


def user_login_mentee(request):
    if request.method == "GET":
        form = LogInFormMentee()
        return render(request, template_name="mentorapp/login.html", context={"form": form})
    elif request.method == "POST":
        form = LogInFormMentee(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            user_password = form.cleaned_data["user_password"]
            user = authenticate(request, username=user_name, password=user_password)
            if user:
                login(request, user)
                messages.success(request, "Ai fost autentificat !")
                return redirect('home')
        messages.error(request, "Autentificare nereusita !")
        return render(request, template_name="mentorapp/login.html",context={"form": form})


def mentor_signup(request):
    if request.method == "GET":
        form = RegisterMentor()
        return render(request, template_name="mentorapp/signup_mentor.html", context={"form": form})
    elif request.method == "POST":
        form = RegisterMentor(request.POST)
        if form.is_valid():   # validare if info is correct
            user = form.save(commit=False)
            user.is_mentor = True
            user.save()
            login(request, user)  # autentificare
            return redirect('all_mentors')
        else:
            print("Forma invalida")
            print(form.errors)
            messages.error(request, "Your password is incorrect!")
            return redirect('signup_mentor')


def mentee_signup(request):
    if request.method == "GET":
        form = RegisterMentee()
        return render(request, template_name="mentorapp/signup_mentee.html", context={"form": form})
    elif request.method == "POST":
        form = RegisterMentee(request.POST)
        if form.is_valid():   # validare if info is correct
            user = form.save()
            login(request, user)  # autentificare
            return redirect('home')
        else:
            print("Forma invalida")
            print(form.errors)
            messages.error(request, "Your password is incorrect!")
            return redirect('signup_mentee')

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out !")
    return redirect('login')


def show_all_mentors(request):
    all_mentors = UserMentor.objects.all()
    mentors_context = {
        "mentors": all_mentors,
        "nr_mentors": all_mentors.count()
    }
    return render(request, template_name='mentorapp/showallmentors.html', context=mentors_context)


def show_all_mentees(request):
    all_mentees = UserMentee.objects.all()
    mentees_context = {
        "mentees": all_mentees,
        "nr_mentees": all_mentees.count()
    }
    return render(request, template_name='mentorapp/showallmentees.html', context=mentees_context)


