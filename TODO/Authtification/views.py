from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login

def enter(request):
    if request.user.is_authenticated:
        return redirect("main")
    else:
        return redirect("reg", mode= 'register')
    
def authtificate(request, mode):
    if mode == "register":
        form = forms.UserCreationForm()
        flag = False
    else:
        form = forms.AuthenticationForm()
        flag = False
    return render(request, "Auntification/index.html", {"flag":flag, "form":forms})

def register(request):
    form = forms.UserCreationForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        redirect("main")
    redirect("auth")

def user_login(request):
    form = forms.AuthenticationForm(data=request.POST)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authtificate(request, username=username, password=password)
        login(request, user) 
        redirect("main")
    redirect("auth")
