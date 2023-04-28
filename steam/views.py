from django.shortcuts import render
from .models import Game

def home(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'index.html', {'games': games})
