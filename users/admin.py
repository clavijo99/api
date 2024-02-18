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

@admin.register(Modality)
class ModalityAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('career_id','day','credits')

@admin.register(Matter)
class MatterAdmin(admin.ModelAdmin):
    list_display = ('name','career_id','semester_id','credits')

@admin.register(Lounge)
class LoungeAdmin(admin.ModelAdmin):
    list_display = ('name',)