from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self) -> str:
        return self.name
        

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits = 20,decimal_places=2)
    quantity = models.IntegerField(blank=True, default=1)
    recommend = models.TextField(blank=True)
    image = models.ImageField(upload_to='productImages', default='default.jpg') 
    datecreated = models.DateTimeField(auto_now_add=True)  #không thể chỉnh sữa ngày tạo và khởi tạo thời gian tạo
    
    def __str__(self) -> str:
        return self.name

# class Cart(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     def __str__(self) -> str:
#         return self.product.name 
    
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