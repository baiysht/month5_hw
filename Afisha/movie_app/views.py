from django.template.defaultfilters import title
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
from movie_app.models import Director, Movie, Review, MoviesReviews
from movie_app.serializers import (DirectorSerializer, MovieSerializer, ReviewSerializer,
                                   MoviesReviewsSerializer, DirectorMovies, DirectorValidateSerializer,
                                   MovieValidateSerializer, ReviewValidateSerializer)
from django.db import transaction




class directors_list_create_api_view(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class director_detail_api_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'


class movies_list_create_api_view(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )
        movie.save()
        return Response(MovieSerializer(movie).data, status=status.HTTP_201_CREATED)


class movie_detail_api_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'


class reviews_list_create_api_view(generics.ListCreateAPIView):
        queryset = Review.objects.all()
        serializer_class = ReviewSerializer

        def post(self, request, *args, **kwargs):
            serializer = ReviewValidateSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
            text = serializer.validated_data.get('text')
            movie_id = serializer.validated_data.get('movie_id')
            stars = serializer.validated_data.get('stars')
            review = Review.objects.create(
                text=text,
                movie_id=movie_id,
                stars=stars
            )
            return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)


class review_detail_api_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        review_detail = self.get_object()
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        review_detail.text = serializer.validated_data.get('text')
        review_detail.movie_id = serializer.validated_data.get('movie_id')
        review_detail.stars = serializer.validated_data.get('stars')
        review_detail.save()
        return Response(ReviewSerializer(review_detail).data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes(IsAuthenticated)
def movies_reviews_list_api_view(request):
    movies_reviews = MoviesReviews.objects.all()
    data = MoviesReviewsSerializer(movies_reviews, many=True).data
    return Response(data=data,
                    status=status.HTTP_200_OK)