from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

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
    
class Gender(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name
    
class ImageProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default=None, null=True, blank=True)
    name = models.CharField(max_length=100, default=None, null=True, blank=True)
    image= models.ImageField(upload_to='productImages')  
    def __str__(self) -> str:
        return self.name  

class Size(models.Model):
    name = models.CharField(max_length=10)    
    def __str__(self) -> str:
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='colorImages')
    
    def __str__(self) -> str:
        return self.name
    
class Variants(models.Model):
    name = models.CharField(max_length=100,default=None, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, default=None, null=True, blank=True)
    size = models.ManyToManyField(Size, default=None, null=True, blank=True)
    color = models.ManyToManyField(Color, default=None, null=True, blank=True)
    imageProduct = models.ManyToManyField(ImageProduct, default=None, null=True, blank=True)
    # quantity = models.IntegerField(blank=True, default=0)
    # price = models.DecimalField(max_digits = 20,decimal_places=2,default=None, null=True, blank=True)

