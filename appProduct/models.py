from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self) -> str:
        return self.name
        
class Gender(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, default=None, null=True, blank=True)
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

