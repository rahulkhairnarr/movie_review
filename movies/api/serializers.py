from rest_framework import serializers
from movies.models import Movie, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','user','comment', 'rating','content_type', 'object_id']


class MoviesSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'summary_text', 'director','review']
        

class MoviesOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'summary_text', 'director']

