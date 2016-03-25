from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from django.conf import settings
from rest_framework import viewsets, mixins, permissions
from .serializers import RatingSerializer
from .models import Rating
from bcServer.lessons.models import Lesson
# Create your views here.

class RatingViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        lessonInstance = Lesson.objects.get(id = self.kwargs['lessonID'])
        serializer.save(user=self.request.user, lesson = lessonInstance)

    def get_queryset(self):
        lessonID = self.kwargs['lessonID']
        return Rating.objects.filter(user=self.request.user, lesson=lessonID)
