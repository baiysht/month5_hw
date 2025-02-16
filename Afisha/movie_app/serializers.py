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

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=2, max_length=255)

class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, min_length=1, max_length=255)
    description = serializers.CharField(required=True, min_length=1, max_length=255)
    duration = serializers.IntegerField(required=True)
    director_id = serializers.CharField(required=True)

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, min_length=1, max_length=255)
    movie_id = serializers.IntegerField(required=True)
    stars = serializers.IntegerField(required=True, min_value=1, max_value=10)

