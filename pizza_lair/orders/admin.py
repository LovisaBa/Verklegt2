from django.contrib import admin
from orders.models import *
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, AuthorAdmin)
admin.site.register(OrderItem, AuthorAdmin)
