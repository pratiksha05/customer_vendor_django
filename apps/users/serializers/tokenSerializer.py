from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.users.models import *


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['email'] = user.email
        token['role'] = user.role.title
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        return token
