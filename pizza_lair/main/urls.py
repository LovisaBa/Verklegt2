from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/pizzas
    path('', views.index, name="main_index"),
    path('about/', views.about, name="about")
]
