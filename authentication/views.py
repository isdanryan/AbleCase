from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm

def UserLogin(request):
    if not request.user.is_authenticated:
        form = UserLoginForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username,
                                    password=password)
                if user is not None:
                    login(request, user)
                    print("Login successful, taking you to cases")
                    return redirect("/cases")
                else:
                    print("Incorrect Username or password")

        return render(request, 'authentication/user_login.html', {'form': form})
    else:
        return redirect("/")


def UserSignOut(request):
    logout(request)
    return redirect('/login')
