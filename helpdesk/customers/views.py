from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from customers.forms import UserLoginForm, UserRegistrationForm
from customers.models import Profile


def index(request):
    return render(request, 'customers/home.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('customers:home')
    else:
        form = UserLoginForm()

    return render(request, 'customers/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('customers:login')


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            login(request, new_user)
            return redirect('customers:home')
    else:
        form = UserRegistrationForm()

    return render(request, 'customers/register.html', {'form': form})


def profile_detail(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'customers/profile/detail.html', {'user': user})
