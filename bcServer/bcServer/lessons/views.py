from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, mixins, permissions, serializers

from .models import Lesson, Submit

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
class SubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submit

class LessonViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class SubmitViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = SubmitSerializer
    def get_queryset(self):
        lessonID = self.kwargs['lessonID']
        return Submit.objects.filter(lesson=lessonID)
