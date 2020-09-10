from django.db import transaction
from rest_framework import serializers
from apps.users.models import UserRole, Product, OrderItem


class UserRoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ("id", "title", 'is_active')


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", 'price')


class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("id", "product", 'order', 'status', 'quantity', 'price', 'is_accepted', 'is_active', 'is_deleted')

    def create(self, validated_data):
        quantity = validated_data.get('quantity', 0)
        product = validated_data.get('product')
        with transaction.atomic():
           obj =  OrderItem.objects.create(**validated_data)
        return obj
