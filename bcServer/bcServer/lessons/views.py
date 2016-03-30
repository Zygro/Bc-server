from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.apps import apps

from django.conf import settings

from rest_framework import viewsets, mixins, permissions

from rest_framework.response import Response
from .forms import SubmitForm
from .serializers import CommentSerializer, LessonSerializer, SubmitSerializer
from .models import Comment, Lesson, Submit
from bcServer.user.models import UserLessonWrapper
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
    def get_queryset(self):
        player_progress = apps.get_model('stats','UserStat').objects.get(user=self.request.user).progress
        return Lesson.objects.filter(number__lte = player_progress)

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
        wrapper = UserLessonWrapper.objects.filter(lesson = lessonInstance, user = self.request.user)
        if len(wrapper) == 0:
            w = UserLessonWrapper (
                lesson = lessonInstance,
                user = self.request.user
            )
            w.save()
        res = compare_files(lessonInstance.correct_solution, self.request.POST.get('submittedFile'))
        if res:
            wrapper = UserLessonWrapper.objects.get(lesson = lessonInstance, user = self.request.user)
            print(wrapper.completed)
            if not(wrapper.completed):
                wrapper.completed=True
                wrapper.save()
                userStat = apps.get_model('stats','UserStat').objects.get(user = self.request.user)
                userStat.progress += 1
                userStat.save()
        serializer.save(user = self.request.user, lesson = lessonInstance, result = res)


    def get_queryset(self):
        userID = self.request.user
        lessonID = self.kwargs['lessonID']
        return Submit.objects.filter(lesson=lessonID, user=userID)
