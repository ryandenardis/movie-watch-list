from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f'Review of {self.movie.title} - Rating: {self.rating}'


class Ledger(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watch_date = models.DateField()
    user = models.CharField(max_length=100)

    def __str__(self):
        return f'Watch entry for {self.movie.title} by {self.user} on {self.watch_date}'
