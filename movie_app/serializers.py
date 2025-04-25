from rest_framework import serializers
from .models import Movie, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    # movie_reviews = ReviewSerializer(many=True, read_only=True)
    # movie_reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # movie_reviews = serializers.SlugRelatedField(many=True, read_only=True, slug_field='comment')
    # movie_reviews = serializers.StringRelatedField(many=True, read_only=True)
    movie_reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='review-detail', lookup_field='pk')

    class Meta:
        model = Movie
        fields = '__all__'