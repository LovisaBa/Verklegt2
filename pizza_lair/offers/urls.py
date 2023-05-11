from django.urls import path
from . import views
urlpatterns = [
    # http://localhost:8000/pizzas
    path('', views.index, name="offers_index"),
    path('offer/<int:offer_id>', views.get_offer, name='offer_details'),
    path('discount/<int:offer_id>', views.get_discount, name='discount_details')
]

