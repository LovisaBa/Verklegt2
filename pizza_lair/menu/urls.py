from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/pizzas
    path('', views.index, name="menu_index"),
    path('<int:id>', views.get_pizza_by_id, name='pizza-details'),
    path('<int:id>', views.get_drink_by_id, name='drink-details'),
]
