from django.contrib import admin
from django.urls import path, include
from .views import all_movies, MovieDetailView, add_movie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie_app.urls')),
    path('movies/', all_movies, name='all_movies'),
    path('movies/<int:movie_id>/', MovieDetailView.as_view(), name='movie_detail'),
    path('add_movie/', add_movie, name='add_movie'),
    path('admin/', admin.site.urls),
]
