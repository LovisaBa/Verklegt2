from django.urls import path
from . import views
urlpatterns = [
    # http://localhost:8000/pizzas
    path('', views.index, name="offers_index"),
    path('offer/<int:id>', views.get_offer_by_id, name='offer_details'),
    path('discount/<int:id>', views.get_discount_by_id, name='discount_details'),
]

