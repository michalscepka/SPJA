from django.urls import path

from . import views

'''urlpatterns = [
    #path('index/<int:my_id>', views.index, name='index')
    path('index/', views.index, name='index')
]'''

urlpatterns = [
    path('', views.index, name='index'),
]

