from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from rest_framework import serializers, validators
from .models import UserLessonWrapper

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

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length = 36,
        style={'placeholder':'Username'}
    )
    password = serializers.CharField(
        max_length=36,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

class WrapperSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLessonWrapper
