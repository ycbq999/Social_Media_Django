from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.
def user_login(request):


    if request.method == "POST":
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