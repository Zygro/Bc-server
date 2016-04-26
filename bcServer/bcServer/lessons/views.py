from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.apps import apps
from django.conf import settings
from django.shortcuts import redirect

from rest_framework.decorators import list_route, api_view
from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, JSONParser, MultiPartParser, FormParser

from .forms import SubmitForm
from .serializers import CommentSerializer, LessonSerializer, SubmitSerializer, HintSerializer, SingleLessonSerializer
from .models import Comment, Lesson, Submit, Hint
from bcServer.user.models import UserLessonWrapper
from .helpers import compare_files

Base_url = '127.0.0.1:8000/'

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
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)
    serializer_class = LessonSerializer
    def get_queryset(self):
        player_progress = apps.get_model('stats','UserStat').objects.get(user=self.request.user).progress
        return Lesson.objects.filter(number__lte = player_progress).order_by('number')
    def show(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            return Response(template_name='lessonslist.html')
        return response
    def singleLesson(self, request, *args, **kwargs):
        player_progress = apps.get_model('stats','UserStat').objects.get(user=self.request.user).progress
        lesson = Lesson.objects.get(id=self.kwargs['lessonID'])
        wrapper = UserLessonWrapper.objects.filter(lesson = lesson, user = self.request.user)
        if len(wrapper) == 0:
            w = UserLessonWrapper (
                lesson = lesson,
                user = self.request.user
            )
            w.save()
        if lesson.number > player_progress:
            return Respone(status=status.HTTP_400_BAD_REQUEST)
        serializer = SingleLessonSerializer(lesson)
        return Response(serializer.data)
    def downloadInputs(self, request, *args, **kwargs):
        #player_progress = apps.get_model('stats','UserStat').objects.get(user=self.request.user).progress
        lesson = Lesson.objects.get(id=self.kwargs['lessonID'])
        #if lesson.number > player_progress:
        #    return Respone(status=status.HTTP_400_BAD_REQUEST)
        response = HttpResponse(lesson.inputs, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=%s' % lesson.inputs
        return response


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
        res = compare_files(lessonInstance.correct_solution, self.request.FILES['submittedFile'])
        if res=="OK":
            wrapper = UserLessonWrapper.objects.get(lesson = lessonInstance, user = self.request.user)
            if not(wrapper.completed):
                wrapper.completed=True
                wrapper.save()
                if not(lessonInstance.optional):
                    userStat = apps.get_model('stats','UserStat').objects.get(user = self.request.user)
                    userStat.progress += 1
                    userStat.save()
        serializer.save(user = self.request.user, lesson = lessonInstance, result = res)

    def get_queryset(self):
        userID = self.request.user
        lessonID = self.kwargs['lessonID']
        return Submit.objects.filter(lesson=lessonID, user=userID)

class HintViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = HintSerializer
    def get_queryset(self):
        lesson = Lesson.objects.get(id=self.kwargs['lessonID'])
        wrapper = UserLessonWrapper.objects.get(lesson = lesson, user = self.request.user)
        return lesson.hint_set.filter(number__lte = wrapper.hints_used)

    @list_route()
    def get_new_hint(self, request, *args, **kwargs):
        lesson = Lesson.objects.get(id=self.kwargs['lessonID'])
        wrapper = UserLessonWrapper.objects.get(lesson = lesson, user = self.request.user)
        if wrapper.hints_used < len(lesson.hint_set.all()):
            wrapper.hints_used += 1
            wrapper.save()
        hints = Hint.objects.filter(lesson = lesson, number__lte = wrapper.hints_used)
        serializer = HintSerializer(hints, many = True)
        return Response(serializer.data)

class Lessonslist(APIView):
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = 'lessonslist.html'
    def get(self, request):
        player_progress = apps.get_model('stats','UserStat').objects.get(user=self.request.user).progress
        queryset = Lesson.objects.filter(number__lte = player_progress).order_by('number')

        return Response({'lessons': queryset, 'base_url':Base_url})

class SingleLessonView(APIView):
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = 'singlelesson.html'
    parser_classes = (MultiPartParser,)
    def get(self, request, *args, **kwargs):
        return Response(template_name='singlelesson.html')
