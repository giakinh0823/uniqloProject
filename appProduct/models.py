from django.db import models
from django.contrib.auth.models import User

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
    quantity = models.IntegerField()
    datecreated = models.DateTimeField(auto_now_add=True)  #không thể chỉnh sữa ngày tạo và khởi tạo thời gian tạo
    
    def __str__(self) -> str:
        return self.name