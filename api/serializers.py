from .models import Article
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "description"]


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", "username", "password"]

#         extra_kwargs = {"password": {"write_only": True, "required": True}}


# def create(self, validated_data):
#     user = User.objects.create_user(**validated_data)
#     Token.objects.create(user=user)
#     return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def create(self, validated_data):
        # Create the user, which should hash the password automatically
        user = User.objects.create_user(**validated_data)

        # Create the token for the user
        Token.objects.create(user=user)

        return user
