from django.db import models
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.apps import apps
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status, mixins, serializers, validators
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField (
        max_length=50,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username','email', 'first_name', 'last_name'
        )
        read_only_fields = ('id')


    def create(self, validated_data):
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
            )

            user.set_password(validated_data['password'])
            user.save()
            apps.get_model('stats', 'UserStat')(user=user).save()
            return user
'''
@api_view(['POST'])
def register(request):
    VALID_USER_FIELDS = [f.name for f in get_user_model()._meta.fields]
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        user_data = {field: data for (field, data) in request.data.items() if field in VALID_USER_FIELDS}

        user = get_user_model().objects.create_user(
            **user_data
        )
        return Response(UserSerializer(instance=user).data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
'''
class UserViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin
):
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
        if user is None:
            return self._fail_login_response('Incorrect credentials.')
        return self._successful_login_response(user)

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
    def _successful_login_response(self, user):
        token = Token.objects.get_or_create(user=user)[0]
        return Response({'token': token.key})

    def _fail_login_response(self, detail='BAD REQUEST'):
        return Response({'detail': detail}, status=status.HTTP_400_BAD_REQUEST)
