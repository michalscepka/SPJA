from django.contrib import admin

from .models import Developer, Category, Game, Review

admin.site.register(Developer)
admin.site.register(Category)
admin.site.register(Game)
admin.site.register(Review)
