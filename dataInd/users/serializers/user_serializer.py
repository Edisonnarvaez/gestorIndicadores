from rest_framework import serializers
from users.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'username', 'email', 'phone', 'company', 'department', 'role', 'status', 'creationDate', 'updateDate', 'lastLogin']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
