from django.urls import path
from . import views

app_name= 'appProduct'

urlpatterns = [
    path('product/', views.product , name ='product'),
    path('createproduct/', views.createproduct, name='createproduct'),
    path('productuser/', views.productuser, name='productuser'),
    path('product/<int:product_pk>/', views.detailproduct, name ='detailproduct'),
    path('product/<int:product_pk>/editproduct/', views.editproduct, name ='editproduct'),
    path('product/<int:product_pk>/deleteproduct/', views.deleteproduct, name="deleteproduct")
]
