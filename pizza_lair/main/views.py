from django.shortcuts import render

# Create your views here.


def index(request):
    """Renders the main site of the webpage."""
    return render(request, 'main/index.html',)


def about(request):
    """Renders the 'about us' site."""
    return render(request, 'main/about_us.html')
