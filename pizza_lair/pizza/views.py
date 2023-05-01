from django.shortcuts import render

# Create your views here.
pizzas = [
    {'name':'Margarita', 'price':2500},
    {'name':'Pepperoni', 'price':3000}
          ]

def index(request):
    return render(request, 'pizza/index.html', context={'pizzas':pizzas})
