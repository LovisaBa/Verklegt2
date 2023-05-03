from django.contrib import admin
from users.models import *
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Users, AuthorAdmin)
admin.site.register(Payments, AuthorAdmin)
admin.site.register(UserPayment, AuthorAdmin)
