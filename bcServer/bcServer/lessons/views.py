from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from django.conf import settings

from rest_framework import viewsets, mixins, permissions

from rest_framework.response import Response
from .forms import SubmitForm
from .serializers import CommentSerializer, LessonSerializer, SubmitSerializer
from .models import Comment, Lesson, Submit
from .helpers import compare_files
class CommentViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):

    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        lessonInstance = Lesson.objects.get(id = self.kwargs['lessonID'])
        serializer.save(user=self.request.user, lesson = lessonInstance)

    def get_queryset(self):
        lessonID = self.kwargs['lessonID']
        return Comment.objects.filter(lesson=lessonID)

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
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubmitSerializer

    def perform_create(self, serializer):
        lessonInstance = Lesson.objects.get(id = self.kwargs['lessonID'])
        print (lessonInstance.correct_solution)
        res = compare_files(lessonInstance.correct_solution, self.request.POST.get('submittedFile'))
        serializer.save(user = self.request.user, lesson = lessonInstance, result = res)


    def get_queryset(self):
        userID = self.request.user
        lessonID = self.kwargs['lessonID']
        return Submit.objects.filter(lesson=lessonID, user=userID)
