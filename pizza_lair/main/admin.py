from django.contrib import admin
from main.models import Products
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Products, AuthorAdmin)