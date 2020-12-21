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
    state = models.CharField(default="Waiting", max_length=256)
    totalprice = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.user.username
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    totalprice = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.product.name