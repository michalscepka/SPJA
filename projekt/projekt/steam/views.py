from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Developer, Category, Game, Review
from .forms import ReviewForm
from .filters import GameFilter

def index(request):
    games_list = Game.objects.all()
    games_filter = GameFilter(request.GET, queryset=games_list)
    return render(request, 'steam/index.html', {'filter': games_filter})

def game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    review = ReviewForm()
    return render(request, 'steam/game.html', {'game': game, 'review': review})

def developer(request, developer_id):
    developer = get_object_or_404(Developer, pk=developer_id)
    return render(request, 'steam/developer.html', {'developer': developer})

def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'steam/category.html', {'category': category})

def developers(request):
    developer_list = Developer.objects.all()
    context = {'developer_list': developer_list}
    return render(request, 'steam/developers.html', context)

def categories(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return render(request, 'steam/categories.html', context)

def addreview(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_author = review_form.cleaned_data['author_name']
            review_text = review_form.cleaned_data['text']
            review_stars = review_form.cleaned_data['stars']
            review = Review(game=game, author_name=review_author, text=review_text, stars=review_stars)
            review.save()

            return redirect('steam:game', game_id=game.id)
