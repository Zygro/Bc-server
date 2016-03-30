from rest_framework import serializers
from .models import Rating, LessonStat

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'lesson','user', 'fun', 'difficulty')
        read_only_fields = ('id', 'user','lesson')
        unique_together = ('user', 'lesson')

class LessonStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonStat
        fields = ('id', 'lesson', 'avg_fun', 'avg_diff')
        read_only_fields = ('avg_fun', 'avg_diff')
