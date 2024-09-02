from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLoginForm


# User login fucntion
def UserLogin(request):
    # If there is no active session load login page
    # Otherwise redirect user to the dashboard
    if not request.user.is_authenticated:
        form = UserLoginForm(request.POST or None)
        if request.method == "POST":

            # Check and clean the entered data
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username,
                                    password=password)

                # Check user exists and is staff
                if user is not None and user.role == "Staff":
                    login(request, user)
                    return redirect("/")
                else:
                    messages.error(request, "Incorrect username or password")

        return render(request, 'authentication/user_login.html',
                      {'form': form})
    else:
        # Redirect user to dashboard if already logged in
        return redirect("/")


# Signout function
def UserSignOut(request):
    logout(request)
    return redirect('/login')
