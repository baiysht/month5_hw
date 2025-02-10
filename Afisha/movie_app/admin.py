from django.contrib import admin

from movie_app.models import Movie, Director, Review, MoviesReviews, DirectorMovies

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Review)
admin.site.register(MoviesReviews)
admin.site.register(DirectorMovies)