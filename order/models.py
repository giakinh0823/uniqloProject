from django.db import models
from appProduct.models import Product
from django.contrib.auth.models import User


# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=1)
    def __str__(self) -> str:
        return self.product.name 
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(default="XXXXXXX", max_length=256)
    state_choices = (
        ('In Queue', 'In Queue'),
        ('Processing', 'Processing'),
        ('Ready', 'Ready'),
        ('Delivered', 'Delivered'),
        ('Paid', 'Paid'),
        ('Cancelled', 'Cancelled'),
    ) 
    state = models.CharField( max_length=256, choices=state_choices, default=state_choices[0][0])
    totalprice = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return 'Order {}'.format(self.id)
    
    def get_total_cost(self):
        return self.totalprice
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    totalprice = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return '{}'.format(self.id)
    
    def get_cost(self):
        return self.totalprice * self.quantity