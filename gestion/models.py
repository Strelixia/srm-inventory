
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('buyer', 'Buyer'),
        ('supplier','Supplier'),
    ]
    role = models.CharField(max_length= 8, choices= ROLE_CHOICES)
    groups = models.ManyToManyField('auth.Group', related_name= 'custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name= 'custom_user_permissions', blank=True)
    def __str__(self):
            return self.username

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length= 200)
    price = models.DecimalField(max_digits= 10, decimal_places= 2)
    supplier = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
         return self.name

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    def __str__(self):
         return self.user

class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete= models.CASCADE, related_name='buyer_orders')
    supplier = models.ForeignKey(User, on_delete= models.CASCADE, related_name='supplier_orders')
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length= 20, choices= [('PENDING','pending'),('PAID','paid'),('DELIVERED','delivered')])
    order_date = models.DateField(auto_now_add= True)
    def __str__(self):
         return self.status, self.product
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits= 10, decimal_places= 2)
    status = models.CharField(max_length= 20, choices= [('PENDING','pending'),('PAID','paid'),('DELIVERED','delivered')])
    payment_date = models.DateTimeField()
    def __str__(self):
         return self.status, self.amount

class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete= models.CASCADE)
    status = models.CharField(max_length= 20, choices= [('IN TRANSIT','In transit'),('DELIVERED','Delivered')])
    delivery_date = models.DateTimeField()
    def __str__(self):
         return self.status, self.order
    