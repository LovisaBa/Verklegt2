from django.contrib import admin
from offers.models import *
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Offer, AuthorAdmin)
admin.site.register(Discount, AuthorAdmin)
admin.site.register(PizzaOffer, AuthorAdmin)
