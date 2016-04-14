from rest_framework import serializers
from .models import Lesson, Submit, Comment, Hint

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'number','pub_date', 'optional','name')
        model = Lesson

class SubmitSerializer(serializers.ModelSerializer):
    submittedFile = serializers.FileField(
        label=''
    )
    class Meta:
        model = Submit
        fields = ('id', 'lesson', 'submittedFile','user', 'result')
        read_only_fields = ('id', 'user','lesson', 'result')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields = ('id', 'lesson', 'text','user')
        read_only_fields = ('id', 'user','lesson')

class HintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hint
        fields = ('id','lesson','text')

class SingleLessonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'number','pub_date', 'optional','name', 'problem', 'inputs')
        model = Lesson
