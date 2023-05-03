from django.contrib import admin
from offers.models import *
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Offers, AuthorAdmin)
admin.site.register(Discounts, AuthorAdmin)
admin.site.register(PizzaOffers, AuthorAdmin)
admin.site.register(PizzasInOffers, AuthorAdmin)
