from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Developer, Category, Game, Review

def index(request):
    games_list = Game.objects.all()
    context = {'games_list': games_list}
    return render(request, 'steam/index.html', context)

def game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'steam/game.html', {'game': game})

def developer(request, developer_id):
    developer = get_object_or_404(Developer, pk=developer_id)
    return render(request, 'steam/developer.html', {'developer': developer})

def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'steam/category.html', {'category': category})
