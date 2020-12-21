from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name= 'appProduct'

urlpatterns = [
    path('product/', views.product , name ='product'),
    path('product/addcart/', views.addcart , name ='addcart'),
    path('createproduct/', views.createproduct, name='createproduct'),
    path('productuser/', views.productuser, name='productuser'),
    path('product/<int:product_pk>/addcart/', views.addcartdetail, name ='detailproductaddcart'),
    path('product/<int:product_pk>/', views.detailproduct, name ='detailproduct'),
    path('product/<int:product_pk>/editproduct/', views.editproduct, name ='editproduct'),
    path('product/<int:product_pk>/deleteproduct/', views.deleteproduct, name="deleteproduct"),
    path('basket/', views.basket , name ="basket"),
    path('checkout/', views.checkout , name ="checkout"),
    path('confirmcheckout/', views.confirmcheckout , name ="confirmcheckout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
