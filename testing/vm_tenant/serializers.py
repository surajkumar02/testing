from django.contrib.auth.models import User
from rest_framework import serializers
from .models import SocialUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields='__all__'

class SocialUserSerializer(serializers.ModelSerializer):

    class Meta:
        model=SocialUser
        fields='__all__'