from django.shortcuts import render
from .forms import LoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required   
from .models import Profile
from .forms import UserEditForm, ProfileEditForm
from posts.models import Post

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
    current_user = request.user
    posts = Post.objects.filter(user=current_user)
    profile = Profile.objects.filter(user=current_user).first()
    return render(request, "users/index.html", {"posts": posts, "profile": profile})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, "users/register_done.html", {"new_user": new_user})
        
    else:
        user_form = UserRegisterForm()
    return render(request, "users/register.html", {"user_form": user_form})

@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        
    return render(request, "users/edit.html", {"user_form": user_form, "profile_form": profile_form})
