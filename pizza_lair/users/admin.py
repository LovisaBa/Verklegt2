from django.contrib import admin
from users.models import *
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Country, AuthorAdmin)
admin.site.register(Profile, AuthorAdmin)
admin.site.register(Payment, AuthorAdmin)
