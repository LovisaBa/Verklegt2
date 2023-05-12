from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from users.forms.user_form import ProfileForm
from users.models import Profile

# Create your views here.


def create_user(request):
    """Allows a user to create a new user."""
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User successfully created!')
            return redirect('login')
        else:
            return render(request, 'users/create_user.html', {
                'form': form
            })
    return render(request, 'users/create_user.html', {
        'form': UserCreationForm()
    })


def profile(request):
    """Returns a render of the users profile. It can create a profile
        for a logged-in user, or allows a user to update their profile"""
    user_profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=user_profile, data=request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            messages.success(request, 'Profile successfully updated!')
        else:
            return render(request, 'users/profile.html', {
                'form': form
            })
    return render(request, 'users/profile.html', {
        'form': ProfileForm(instance=user_profile)
    })
