from django.shortcuts import render
from users.forms.user_form import UserCreateForm
# Create your views here.


def index(request):
    return render(request, 'users/index.html')


def create_user(request):
    if request.method == 'POST':
        somthing
    else:
        form = UserCreateForm()
    return render(request, 'users/create_user.html', {
        'form': form
    })


def login(request):
    return render(request, 'users/login.html')
