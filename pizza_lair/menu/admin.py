from django.contrib import admin
from menu.models import *
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(PizzaType, AuthorAdmin)
admin.site.register(Pizza, AuthorAdmin)
admin.site.register(Ingredient, AuthorAdmin)
admin.site.register(Drink, AuthorAdmin)
admin.site.register(PizzaImage, AuthorAdmin)
admin.site.register(DrinkImage, AuthorAdmin)
