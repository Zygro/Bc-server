from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, mixins, permissions, serializers

from .models import Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson

class LessonViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
