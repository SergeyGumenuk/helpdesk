from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from customers.forms import UserLoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
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


def profile_edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile update successfully')
        else:
            messages.error(request, 'Updating error')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'customers/profile/edit.html', {'user_form': user_form,
                                                           'profile_form': profile_form})


def profile_delete(request):
    user = request.user
    logout(request)
    User.objects.filter(pk=user.id).update(is_active=False)
    Profile.objects.filter(user=user).delete()
    return redirect('customers:home')
