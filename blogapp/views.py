from django.shortcuts import render,redirect
from django.http import HttpResponse
from .import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
# Create your views here.

form = forms.Blogform()

def create(request):
    if request.method == 'POST':
        form = forms.Blogform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('/showblog/')

    else:
        form = forms.Blogform()
        return render(request, 'createblog.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(data=request.POST)
        if signup_form.is_valid():
            signup_form.save()
            # user = signup_form.get_user()
            # login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': signup_form})
    else:
        signup_form = UserCreationForm()
        return render(request,'signup.html',{'form': signup_form})

def login(request):
    if request.method == 'POST':
        Login_form = AuthenticationForm(data=request.POST)
        if Login_form.is_valid():
            user = Login_form.get_user()
            login(request,user)
            return redirect('/')
        else:
            return render(request, 'Login.html', {'form': Login_form})
    else:
        Login_form = AuthenticationForm()
        return render(request,'Login.html',{'form':Login_form})