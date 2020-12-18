from django.urls import path
from . import views

app_name= 'appProduct'

urlpatterns = [
    path('product/', views.product , name ='product'),
    path('createproduct/', views.createproduct, name='createproduct'),
    path('productuser/', views.productuser, name='productuser'),
    path('product/<int:product_pk>/', views.detailproduct, name ='detailproduct'),
]
