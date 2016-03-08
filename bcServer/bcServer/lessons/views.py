from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from django.conf import settings

from rest_framework import viewsets, mixins, permissions, serializers

from rest_framework.response import Response
from .forms import SubmitForm
from .models import Lesson, Submit

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson

class SubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submit
        fields = (
            'id', 'user', 'lesson', 'submittedFile'
        )
        read_only_fields = ('id')

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
    serializer_class = SubmitSerializer
    def get_queryset(self):
        lessonID = self.kwargs['lessonID']
        return Submit.objects.filter(lesson=lessonID, user=self.request.user)

"""    def submitfile (self, request, *args, **kwargs):
        if request.method == 'POST':
            form = SubmitForm(request.POST, request.FILES)
            if form.is_valid():
                print('valid')
                newSubmit = Submit(
                    user = self.request.user,
                    lessonID = self.kwargs['lessonID'],
                    submitfile = request.FILES['submitfile']
                    )
                print('hello')
                newSubmit.save()

                return Response({'status': 'ok'})
            else:
                form = SubmitForm()

            submits = Submit.objects.all()

            return Response(submits)"""
