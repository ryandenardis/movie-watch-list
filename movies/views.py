from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie

# Movie list view
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

# Movie create view
def movie_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        release_date = request.POST['release_date']
        movie = Movie(title=title, release_date=release_date)
        movie.save()
        return redirect('movie_detail', movie_id=movie.id)
    return render(request, 'movies/movie_form.html')

# Movie edit view
def movie_edit(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.title = request.POST['title']
        movie.release_date = request.POST['release_date']
        movie.save()
        return redirect('movie_detail', movie_id=movie.id)
    return render(request, 'movies/movie_form.html', {'movie': movie})

# Movie detail view
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

# Movie review view
def movie_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        review = request.POST['review']
        # Save review logic (not implemented)
        return redirect('movie_detail', movie_id=movie.id)
    return render(request, 'movies/movie_review.html', {'movie': movie})
