from rest_framework import serializers
from .models import Rating, LessonStat

class RatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    lesson = serializers.PrimaryKeyRelatedField(read_only=True, default=None)

    class Meta:
        model = Rating
        fields = ('id', 'lesson','user', 'fun', 'difficulty')
        read_only_fields = ('id')

class LessonStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonStat
        fields = ('id', 'lesson', 'avg_fun', 'avg_diff')
        read_only_fields = ('avg_fun', 'avg_diff')

class DueToChangeSerializer(serializers.ModelSerializer):
    lesson = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = LessonStat
        fields = ['lesson','avg_fun','avg_diff']
