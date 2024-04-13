""" Managing URLs for the 'music_app' in the project """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('signup', views.Signup.as_view(), name='signup'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('music/<str:song_id>', views.Music.as_view(), name='music'),
    path('profile/<str:artist_id>', views.Profile.as_view(), name='profile'),
    path('search', views.Search.as_view(), name='search'),
]
