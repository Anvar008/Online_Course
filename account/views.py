from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register_function(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

@login_required(login_url='login')
def main_function(request):
    return render(request, 'index-login.html')

def login_function(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

@login_required(login_url='login')
def logout_function(request):
    logout(request)
    return redirect('login')
