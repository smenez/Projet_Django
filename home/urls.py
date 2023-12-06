from django.urls import path
from .views import index, game_page, Inscription, classement, memorygame, mortsubite, Connexion


urlpatterns = [
    path('', index, name='index'),
    path('gamemode.html',game_page, name='game_page'),
    path('classement.html', classement, name='classement'),
    path('index.html', index, name='index'),
    path('memory_game.html', memorygame, name='memory_game'),
    path('mortsubite.html', mortsubite, name='mortsubite'),
    path('form.html', Inscription, name='inscription'),
    path('signup.html', Connexion, name='inscription'),
]