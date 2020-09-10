from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class UserRole(models.Model):
    title = models.CharField(max_length=50)
    is_active=models.BooleanField(default=False)


class User(AbstractUser):
    email = models.EmailField('Email', max_length=40)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE, null=True, blank=True, related_name='user_roles',
                                 related_query_name='user_role')
    is_active = models.BooleanField("Active", default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True, related_name='user_orders',
                             related_query_name='user_order')


class OrderItem(models.Model):
    STATUS = (
        ("PLACED", "PLACED"),
        ("ACCEPTED", "ACCEPTED"),
        ("CANCELLED", "CANCELLED")
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True,
                             related_name='user_products', related_query_name='user_product')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='user_orders', related_query_name='user_order')
    status = models.CharField(max_length=50, choices=STATUS, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2, null = True, blank=True)
    is_accepted = models.BooleanField(default = False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default = False)




