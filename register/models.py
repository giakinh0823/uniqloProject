from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #mối quan hệ một một
    
    #additional
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)    
    birth_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    site = models.URLField(blank=True) #blank=true có nghĩa là để trống không cần điền vẫn ok
    avatar = models.ImageField(upload_to='images', blank=True) 
    
    def __str__(self) -> str:
        return self.user.username
    

