from typing import Dict, Any
from django.contrib.auth.models import User
from rest_framework import serializers

__all__ = [
    'serialize_user',
    'UserModelSerializer',
    'UserReadOnlyModelSerializer',
    'UserSerializer',
    'UserReadOnlySerializer'
]

def serialize_user(user: User) -> Dict[str, Any]:
    return {
        'id': user.id,
        'last_login': user.last_login.isoformat() if user.last_login is not None else None,
        'is_superuser': user.is_superuser,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'is_staff': user.is_staff,
        'is_active': user.is_active,
        'date_joined': user.date_joined.isoformat(),
    }

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'last_login',
            'is_superuser',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'date_joined',
        ]

class UserReadOnlyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'last_login',
            'is_superuser',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'date_joined',
        ]
        read_only_fields = fields

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    last_login = serializers.DateTimeField()
    is_superuser = serializers.BooleanField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    is_active = serializers.BooleanField()
    date_joined = serializers.DateTimeField()


class UserReadOnlySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)