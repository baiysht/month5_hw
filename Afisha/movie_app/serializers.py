from rest_framework import serializers
from movie_app.models import Director, Movie, Review, MoviesReviews, DirectorMovies

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorMovies
        #fields = '__all__'
        #fields = ['id', 'title', 'price']
        #exclude = ['id','is_active']
        fields = 'director movies'.split()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        #fields = '__all__'
        #fields = ['id', 'title', 'price']
        #exclude = ['id','is_active']
        fields = 'id title description duration director'.split()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        #fields = '__all__'
        #fields = ['id', 'title', 'price']
        #exclude = ['id','is_active']
        fields = 'id text movie stars'.split()

class MoviesReviewsSerializer(serializers.ModelSerializer):
    review_stars = serializers.SerializerMethodField()
    class Meta:
        model = MoviesReviews
        fields = 'movie review_stars'.split()

    def get_review_stars(self, movie):
        return [review.stars for review in movie.reviews.all()]

