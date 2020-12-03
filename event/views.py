from django.shortcuts import render
from .models import Evento
# Create your views here.
def event(request):
    events = Evento.objects.all()
    return render(request, "event/event.html", {'events':events})