from rest_framework import serializers
from users.models.user import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            'id', 'firstName', 'lastName', 'username', 'email', 'phone', 
            'company', 'department', 'role', 'status', 'creationDate', 
            'updateDate', 'lastLogin', 'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True},  # Asegura que las contraseñas no se devuelvan en las respuestas
        }


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)  # Encripta la contraseña
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)  # Encripta la contraseña actualizada
        instance.save()
        return instance
    
class LoginSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField(write_only=True)
