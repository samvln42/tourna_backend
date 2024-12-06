from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .models import UserModel
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'email', 'nickname', 'profile_image', 'password']

    def validate(self, attrs):
        password = attrs.get("password")
        if password is None:
            raise serializers.ValidationError("Password is required.")
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return attrs

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):

        password = validated_data.get("password")  # Get password value
        if password:  # Run only if password value exists
            user = super().update(instance, validated_data)
            user.set_password(password)
            user.save()
        elif not password:
            return instance
        else:
            user = super().update(instance, validated_data)
            user.save()
        return instance

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "email", "nickname", "profile_image"]
        
class ClientUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "email", "nickname", "profile_image"]

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        exclude = ["password",  "last_login"]

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        token["user_id"] = user.id
        token["is_owner"] = user.is_owner
        token["is_admin"] = user.is_admin

        return token

class PostUserSerializer(serializers.Serializer):
    email = serializers.CharField(help_text="email")
    code = serializers.CharField(help_text="Authentication code")
    new_password = serializers.CharField(help_text="change password")
    origin_password = serializers.CharField(help_text="original password")
    password = serializers.CharField(help_text="Password required for login")
    password2 = serializers.CharField(help_text="Password check")
    social = serializers.CharField(help_text="Types for social login transfer URLs")

class GetAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'id', 
            'email', 
            'nickname',
            'profile_image', 
            'is_admin', 
            'is_active'
        ]

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'id',
            'email',
            'nickname',
            'profile_image',
            'is_active'
        ]
