
from rest_framework import serializers
from .models import Lesson, Submit,Comment

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson

class SubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submit
        fields = ('id', 'lesson', 'submittedFile','user')
        read_only_fields = ('id', 'user','lesson')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields = ('id', 'lesson', 'text','user')
        read_only_fields = ('id', 'user','lesson')
