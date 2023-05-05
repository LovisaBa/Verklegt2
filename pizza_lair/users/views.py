from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    return render(request, 'users/index.html')


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'users/create_user.html', {
        'form': UserCreationForm()
    })


def login(request):
    return render(request, 'users/login.html')
