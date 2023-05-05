from django.contrib import admin
from main.models import Product, ProdType
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, AuthorAdmin)
admin.site.register(ProdType, AuthorAdmin)
