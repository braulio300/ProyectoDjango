from django.contrib import admin
from .models import Local, Staff
# Register your models here.

admin.site.register(Local)

class StaffAdmin(admin.ModelAdmin):
    list_display        = ['rut','apellido','nombre','corre']
    list_display_links  = ['rut','apellido','nombre','corre']
    list_filter         = ['nombre']
    search_fields       = ['nombre', 'apellido']

admin.site.register(Staff, StaffAdmin)