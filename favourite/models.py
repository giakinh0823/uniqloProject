from django.db import models
from appProduct.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Favourite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=1)
    def __str__(self) -> str:
        return self.product.name 


