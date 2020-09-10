from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status as http_status_codes
from rest_framework.decorators import permission_classes
from apps.users.models import User, UserRole,Product, OrderItem
from apps.users.helper.jwt_helper import get_my_token
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.users.serializers.UserRoleSerializers import UserRoleSerializers,ProductSerializers,OrderItemSerializers
from apps.users.serializers.RegistrationSerializers import UserRegisterSerializers


class UserViewSets(viewsets.ViewSet):

    @permission_classes([AllowAny])
    def login(self, request):
        params = request.data
        username = params.get('username', None)
        password = params.get('password', None)
        user = authenticate(username=username, password=password)
        if user:
            return Response({
                'message': 'You have been successfully logged in',
                'data': get_my_token({'username': username, 'password': password})
            })
        else:
            return Response({
                'message': 'Invalid Credential'
            }, status=http_status_codes.HTTP_401_UNAUTHORIZED)


class UserRoleView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserRole.objects.filter(is_active=True)
    serializer_class = UserRoleSerializers


class UserRegistratonView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.filter(is_active=True).select_related('role')
    serializer_class = UserRegisterSerializers


class ProductView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class OrderItemView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all().select_related('product', 'order')
    serializer_class = OrderItemSerializers