from django.contrib import admin
from .models import Evento
# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Evento, EventoAdmin)