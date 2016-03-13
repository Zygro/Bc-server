from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status, mixins, serializers, validators
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'password'
        )
        read_only_fields = ('id')

class UserViewSet(
    viewsets.GenericViewSet
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

    def _successful_login_response(self, user):
        token = Token.objects.get_or_create(user=user)[0]
        return Response({'token': token.key})

    def _fail_login_response(self, detail='BAD REQUEST'):
        return Response({'detail': detail}, status=status.HTTP_400_BAD_REQUEST)
