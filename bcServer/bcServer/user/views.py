from django.db import models
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.apps import apps
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import viewsets, permissions, status, mixins
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

from .serializers import UserSerializer, LoginSerializer, WrapperSerializer

from .models import UserLessonWrapper
# Create your views here.

class UserViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
):
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer, renderers.BrowsableAPIRenderer)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def profile(self, request, *args, **kwargs):
        return Response(self.get_serializer(request.user).data)

    def login(self, request, *args, **kwargs):
        if 'username' not in request.data:
            return self._fail_login_response('`username` not specified.')
        if 'password' not in request.data:
            return self._fail_login_response('`password` not specified.')
        user = authenticate(
            username=request.data['username'],
            password=request.data['password'],
        )
        print(User)
        if user is None:
            return self._fail_login_response('Incorrect credentials.')
        return self._successful_login_response(user)

    def logout(self, request, *args, **kwargs):
        token = Token.objects.get(user=self.request.user)
        token.delete()
        return Response({'redirect_url': '/user/login/'})

    def update_profile(self, request, *args, **kwargs):
        user = self.request.user
        print (request.data)
        if 'first_name' in request.data:
            user.first_name = request.data['first_name']
        if 'last_name' in request.data:
            user.last_name = request.data['last_name']
        if 'email' in request.data:
            if len(User.objects.filter(email = request.data['email']))>0:
                return Response({'detail': 'email already used'}, status=status.HTTP_400_BAD_REQUEST)
            else: user.email = request.data['email']
        if 'username' in request.data:
            if len(User.objects.filter(username = request.data['username']))>0:
                return Response({'detail': 'username already used'}, status=status.HTTP_400_BAD_REQUEST)
            else: user.username = request.data['username']
        user.save()
        return Response(self.get_serializer(request.user).data)

    def loginView(self, request, *args, **kwargs):
        loginSerializer = LoginSerializer()
        return Response({'loginSerializer': loginSerializer}, template_name='login.html')

    def displayProfile(self, request, *args, **kwargs):
        return Response(template_name='profile.html')


    def _successful_login_response(self, user):
        token = Token.objects.get_or_create(user=user)[0]
        loginSerializer = LoginSerializer()
        print(token)
        return Response({'token':token.key, 'redirect_url': '/lessons/'}, template_name='login.html')

    def _fail_login_response(self, detail='BAD REQUEST'):
        loginSerializer = LoginSerializer()
        return Response({'loginSerializer': loginSerializer,'detail': detail}, status=status.HTTP_400_BAD_REQUEST, template_name='login.html')

class WrapperViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,):
    serializer_class = WrapperSerializer
    def get_queryset(self):
        userID = self.request.user
        lessonID = self.kwargs['lessonID']
        return UserLessonWrapper.objects.filter(lesson=lessonID, user=userID)
