from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from apps.users.models import UserRole

User = get_user_model()


class UserRegisterSerializers(serializers.ModelSerializer):
    role_id = serializers.IntegerField(required=True)

    class Meta:
        model = User
        fields = ("id", "first_name", 'last_name', 'email','role_id', 'is_active',
                  'is_deleted', 'created_at', 'password', 'updated_at')

    def validate_role_id(self, value):
        if not value:
            raise serializers.ValidationError('Role is required field.')
        instance = UserRole.objects.filter(id = value, is_active = True)[0]
        if not instance:
            raise serializers.ValidationError('Role does not exist.')
        return value

    def validate_password(self, value):
        if len(value) >= 8 and len(value) <=45:
            return value
        else:
            raise serializers.ValidationError('new password must be between 8 to 45 characters long')

    def validate_email(self, value):
        if User.objects.filter(email= value, is_active=True, is_deleted=False).exists():
            raise serializers.ValidationError('email id already exists')
        return value

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['is_staff'] = 0
        validated_data['is_superuser'] = 0
        user = User.objects.create(**validated_data)
        return user
