from django.contrib import admin
from .models import Evento
# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display    = ['title', 'created', 'link']
    list_filter     = ['title', 'created']

admin.site.register(Evento, EventoAdmin)