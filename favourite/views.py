from django.shortcuts import render
from .models import Favourite
from appProduct.models import Product
from django.contrib.auth.models import User
from django.http.response import HttpResponse,JsonResponse


# Create your views here.


def favourite(request):
    favourites = Favourite.objects.all()
    return render(request, 'favourite/favourite.html', {'favourites': favourites})


favourites={}
def addFavourite(request):
    check = 0
    if request.is_ajax():
        id_product = request.POST.get('id')
        productDetail = Product.objects.get(id=id_product)
        if id_product in favourites.keys():
            while id_product in favourites.keys():
                favourites.pop(str(id_product)) 
            request.session['favourites']=favourites
            print(request.session['favourites'])
            check=0
        else:
            itemFavourite = {
                'name': productDetail.name,
                'price': str(productDetail.price),
            #   'image': str(productDetail.image)  #nếu có hình ảnh thì convert sang string
            }
            favourites[id_product]= itemFavourite
            request.session['favourites'] = favourites
            check=1
        favouritesInfo = request.session['favourites']
        if request.user.is_authenticated:
            try:
                favouriteItem = Favourite.objects.get(product = productDetail,user = request.user)
            except Favourite.DoesNotExist:
                favouriteItem = None
            if favouriteItem != None:
                favouriteItem.delete()
                check=0
            else:
                newFavouriteItem = Favourite(user = request.user, product = productDetail,quantity = 1)
                newFavouriteItem.save()
                check=1
            quantity=0
            listFavourite = Favourite.objects.filter(user = request.user)
            for item in listFavourite:
                quantity += int(item.quantity)
            request.session['quantityfavourite']=quantity
        else:
            quantity=0
            for key, value in favouritesInfo.items():
                quantity += 1
                request.session['quantityfavourite']=quantity
        print(request.session['favourites'])
    return JsonResponse({'quantityfavourite': quantity, 'check': check})