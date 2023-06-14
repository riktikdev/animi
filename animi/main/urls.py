from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='mainpage'),
    path('anime/<str:pk>', views.player_page, name='playerpage'),
    path('genres/<str:pk>', views.genres_page, name='genrespage'),
    path('search/<str:pk>', views.search_page, name='searchpage')
]