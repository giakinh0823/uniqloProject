from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name ='order'

urlpatterns = [
    path('product/addcart/', views.addcart , name ='addcart'),
    path('product/<int:product_pk>/addcart/', views.addcartdetail, name ='detailproductaddcart'),
    path('basket/', views.basket , name ="basket"),
    path('basket/<int:cart_pk>/deletecart/', views.deletecart , name ="deletecart"),
    path('checkout/', views.checkout , name ="checkout"),
    path('confirmcheckout/', views.confirmcheckout , name ="confirmcheckout"),
]
