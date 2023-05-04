from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/pizzas
    path('', views.index, name="users_index"),
    path('create_user', views.create_user, name="create_user"),
    path('login', views.login, name="login")
]
