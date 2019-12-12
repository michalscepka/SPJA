from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.db.models import F

from .models import Developer, Category, Game, Review, Choice
from .forms import ReviewForm
from .filters import GameFilter

def index(request):
    games_list = Game.objects.order_by('-release_date')
    games_filter = GameFilter(request.GET, queryset=games_list)
    return render(request, 'steam/index.html', {'title': 'Steam', 'filter': games_filter, 'year': datetime.now().year})

def game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    review_form = ReviewForm()
    stars_count = 0
    if game.review_set.all():
        for review in game.review_set.all():
            stars_count += review.stars
        stars_avg = stars_count / len(game.review_set.all())
    else:
        stars_avg = 'No reviews yet'

    return render(
        request, 'steam/game.html', {
            'game': game,
            'review_form': review_form,
            'stars_avg': stars_avg,
            'title': game.name,
            'year': datetime.now().year})

def developer(request, developer_id):
    developer = get_object_or_404(Developer, pk=developer_id)
    return render(request, 'steam/developer.html', {'developer': developer, 'title': developer.name, 'year': datetime.now().year})

def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'steam/category.html', {'category': category, 'title': category.name, 'year': datetime.now().year})

def developers(request):
    developer_list = Developer.objects.order_by('name')
    return render(request, 'steam/developers.html', {'developer_list': developer_list, 'title': 'Developers', 'year': datetime.now().year})

def categories(request):
    category_list = Category.objects.order_by('name')
    return render(request, 'steam/categories.html', {'category_list': category_list, 'title': 'Categories', 'year': datetime.now().year})

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

def vote(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.likes = F('likes') + 1
    review.save()
    return redirect('steam:game', review.game.id)
