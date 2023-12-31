from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='mainpage'),
    path('anime/<str:pk>', views.player_page, name='playerpage'),
    path('genres/<str:pk>', views.genres_page, name='genrespage'),
    path('search/<str:pk>', views.search_page, name='searchpage'),
    path('terms', views.terms_page, name='terms'),
    path('privacy', views.privacy_page, name='privacy'),
    path('copyright', views.copyright_page, name='copyright'),
    path('ads.txt', views.AdsTxtView.as_view()),
    path('robots.txt', views.RobotsTxtView.as_view()),
    path('sitemap.xml', views.SitemapXmlView.as_view()),
    path('profile/<int:pk>', views.profile_page, name='profilepage')
]