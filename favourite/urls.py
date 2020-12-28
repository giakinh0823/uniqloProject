from django.urls import path
from . import views

app_name = 'favourite'

urlpatterns = [
    path('favourite/', views.favourite, name="favourite"),
    path('product/addfavourite/', views.addFavourite, name="addfavourite"),
    path('favourite/<int:favourite_pk>/deletefavourite/', views.deletefavourite, name="deletefavourite"),
    path('addfavourite/', views.addFavourite, name="addfavourite"),
]
