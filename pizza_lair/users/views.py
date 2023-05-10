from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from users.forms.user_form import ProfileForm
from users.models import Profile

# Create your views here.


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User successfully crated!')
            return redirect('login')
        else:
            messages.error(request, 'There was an error creating the user.')
            return redirect('login')
    return render(request, 'users/create_user.html', {
        'form': UserCreationForm()
    })


def profile(request):
    user_profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=user_profile, data=request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            messages.success(request, 'Profile successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'There was an error updating the user.')
            return redirect('profile')
    return render(request, 'users/profile.html', {
        'form': ProfileForm(instance=user_profile)
    })


def index(request):
    return render(request, 'users/index.html')


def login(request):
    return render(request, 'users/login.html')
