from django.contrib import admin
from menu.models import *
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(PizzaTypes, AuthorAdmin)
admin.site.register(Pizzas, AuthorAdmin)
admin.site.register(PizzaHasType, AuthorAdmin)
admin.site.register(Ingredients, AuthorAdmin)
admin.site.register(PizzaIngredients, AuthorAdmin)
