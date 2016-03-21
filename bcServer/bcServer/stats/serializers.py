from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'lesson','user', 'fun', 'difficulty')
        read_only_fields = ('id', 'user','lesson')
        unique_together = ('user', 'lesson')
