from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

STARS = ((i, '* ' * i) for i in range(1, 11))

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.IntegerField(default=5, choices=STARS)

class MoviesReviews(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    reviews = models.ManyToManyField(Review, blank=True)



class DirectorMovies(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie, blank=True)