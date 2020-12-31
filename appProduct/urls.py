from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name= 'appProduct'

urlpatterns = [
    path('product/', views.product , name ='product'),
    path('product/searchproduct/', views.searchProduct , name ='searchProduct'),
    path('createproduct/', views.createproduct, name='createproduct'),
    path('createproduct/getnameSizeCreate/', views.getnameSizeCreate, name='getnameSizeCreate'),
    path('createproduct/getnameColorCreate/', views.getnameColorCreate, name='getnameColorCreate'),
    path('createproduct/createimageproduct/', views.createimageproduct, name='createimageproduct'),
    path('productuser/', views.productuser, name='productuser'),
    path('product/<int:product_pk>/', views.detailproduct, name ='detailproduct'),
    path('product/<int:product_pk>/getnamecolor/', views.getnamecolor, name ='getnamecolor'),
    path('product/<int:product_pk>/getnameSize/', views.getnameSize, name ='getnameSize'),
    path('product/<int:product_pk>/editproduct/', views.editproduct, name ='editproduct'),
    path('product/<int:product_pk>/editproduct/editcreateimageproduct/', views.editcreateimageproduct, name ='editcreateimageproduct'),
    path('product/<int:product_pk>/deleteproduct/', views.deleteproduct, name="deleteproduct"),
    # path('deleteproduct/<int:product_pk>/', views.deleteproduct, name="deleteproduct"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
