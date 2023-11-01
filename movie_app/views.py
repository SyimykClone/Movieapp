from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Movie
from .forms import MovieForm

def all_movies(request):
    movies = Movie.objects.all()
    return render(request, 'movie_app/all_movies.html', {'movies': movies})

class MovieDetailView(View):
    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        return render(request, 'movie_app/movie_detail.html', {'movie': movie})
    
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_movies')
    else:
        form = MovieForm()
    return render(request, 'movie_app/add_movie.html', {'form': form})