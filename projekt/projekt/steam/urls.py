from django.urls import path

from . import views

app_name = 'steam'
urlpatterns = [
    # ex: /steam/
    path('', views.index, name='index'),
    # ex: /steam/5/
    path('<int:game_id>/', views.game, name='game'),
    # ex: /steam/5/developer/
    path('<int:developer_id>/developer', views.developer, name='developer'),
    # ex: /steam/5/category/
    path('<int:category_id>/category', views.category, name='category'),

    path('<int:game_id>/add_review', views.add_review, name='add_review'),
]
