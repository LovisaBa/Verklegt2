from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/pizzas
    path('', views.index, name="offers_index"),
    path('<int:id>', views.get_offer_by_id, name='offer_details'),
]
