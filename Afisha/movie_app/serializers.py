from rest_framework import serializers
from movie_app.models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        #fields = '__all__'
        #fields = ['id', 'title', 'price']
        #exclude = ['id','is_active']
        fields = 'id name'.split()

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
        fields = 'id text movie'.split()