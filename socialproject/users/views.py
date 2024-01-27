from django.shortcuts import render
from .forms import LoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required   

# Create your views here.
def user_login(request):

    if request.method == "POST":

        print("post post post")
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request, username=form.cleaned_data["username"], password=form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)
                return HttpResponse("Authenticated successfully")
            else:
                return HttpResponse("Invalid username or password")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return render(request, "users/logout.html")
    
@login_required
def index(request):
    return render(request, "users/index.html")  

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            return render(request, "users/register_done.html", {"new_user": new_user})
        
    else:
        user_form = UserRegisterForm()
    return render(request, "users/register.html", {"user_form": user_form})
