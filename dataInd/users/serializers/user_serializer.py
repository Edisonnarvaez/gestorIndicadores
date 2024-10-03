from rest_framework import serializers
from users.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userId', 'firstName', 'lastName', 'username', 'email', 'phone', 'companyId', 'departmentId', 'role', 'status', 'creationDate', 'updateDate', 'lastLogin']

