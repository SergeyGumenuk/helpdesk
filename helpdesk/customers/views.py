from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render

from customers.forms import UserLoginForm


def index(request):
    return HttpResponse('Lets start')


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
    else:
        form = UserLoginForm()

    return render(request, 'customers/login.html', {'form': form})
