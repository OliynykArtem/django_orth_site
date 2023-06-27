from django.urls import path

from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('bishop/', bishop, name='bishop'),
    path('parishes/', parishes, name='parishes'),
    path('parish/<int:parishid>/', parish, name='parish'),

    path('clergy/', clergy, name='clergy'),
    path('clergyman/<int:clergymanid>/', clergyman, name='clergyman'),

    path('photogallery/', photogallery, name='photogallery'),
    path('contacts/', contacts, name='contacts')
]
