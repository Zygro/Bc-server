from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from itertools import chain

from django.conf import settings
from rest_framework import viewsets, mixins, permissions
from .serializers import RatingSerializer, DueToChangeSerializer
from .models import Rating, LessonStat
from bcServer.lessons.models import Lesson
# Create your views here.

class RatingViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        lessonInstance = Lesson.objects.get(id = self.kwargs['lessonID'])
        serializer.save(user=self.request.user, lesson = lessonInstance)
        lessonStat = LessonStat.objects.get(lesson = lessonInstance)
        lessonStat.save()
    def get_queryset(self):
        lessonID = self.kwargs['lessonID']
        return Rating.objects.filter(user=self.request.user, lesson=lessonID)

class DueToChangeViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = DueToChangeSerializer
    def get_queryset(self):
        return LessonStat.objects.filter(avg_fun__lte=3) | LessonStat.objects.filter(avg_diff__lte=2) | LessonStat.objects.filter(avg_diff__gte=4)
