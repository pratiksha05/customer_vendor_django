from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from apps.users.views.users import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'users'

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^login$', UserViewSets.as_view({'post': 'login'})),
    url(r'^user-register', UserRegistratonView.as_view({"post": "create", "get": "list"})),
    url(r'^user-role', UserRoleView.as_view({"post":"create", "get":"list"})),
    url(r'^product', ProductView.as_view({"post":"create", "get":"list"})),
    url(r'^order-item', OrderItemView.as_view({"post":"create", "get":"list"})),
]
