from django.urls import path

from . import views

app_name = 'steam'
urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /5/
    path('<int:game_id>', views.game, name='game'),
    # ex: /5/developer/
    path('<int:developer_id>/developer', views.developer, name='developer'),
    # ex: /5/category/
    path('<int:category_id>/category', views.category, name='category'),
    # ex: /developers/
    path('developers', views.developers, name='developers'),
    # ex: /categories/
    path('categories', views.categories, name='categories'),
    # ex: /5/addreview/
    path('<int:game_id>/addreview', views.addreview, name='addreview'),
    # ex: /5/vote/
    path('<int:review_id>/vote/', views.vote, name='vote')
]
