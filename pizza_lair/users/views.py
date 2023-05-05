from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'users/create_user.html', {
        'form': UserCreationForm()
    })


def index(request):
    return render(request, 'users/index.html')


def login(request):
    return render(request, 'users/login.html')
