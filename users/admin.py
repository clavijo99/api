from django.contrib import admin
from .models import *
@admin.register(UserType)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'type')
    readonly_fields = ('first_name',)