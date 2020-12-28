from django.shortcuts import render, redirect,get_object_or_404
from .models import Favourite
from appProduct.models import Product
from django.contrib.auth.models import User
from django.http.response import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required,user_passes_test


# Create your views here.

def favourite(request):
    favouritelist={}
    if request.user.is_authenticated:
        favouritelist = Favourite.objects.all()
        # quantity=0
        # for item in favouritelist:
        #     quantity += 1
        # request.session['quantityfavourite']=quantity
        # request.session['favourites']=favourites
    else:
        if request.session.get('favourites'):
            favouritelist = request.session['favourites']
            # quantity=0
            # for key, value in favouritelist.items():
            #     quantity += 1
            # request.session['quantityfavourite']=quantity
    return render(request, 'favourite/favourite.html', {'favouritelist': favouritelist})


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
                quantity += 1
            request.session['quantityfavourite']=quantity
        else:
            quantity=0
            if favouritesInfo:
                for key, value in favouritesInfo.items():
                    quantity += 1
            request.session['quantityfavourite']=quantity
        print(request.session['favourites'])
    return JsonResponse({'quantityfavourite': quantity, 'check': check})

def deletefavourite(request, favourite_pk):
    quantity=0
    if request.user.is_authenticated:
        favourite = get_object_or_404(Favourite, pk=favourite_pk, user = request.user)
        favourite.delete()
        favouritelist = Favourite.objects.filter(user = request.user)
        favourites.clear()
        for item in favouritelist:
            quantity += int(item.quantity)
            itemFavourite = {
                'name': item.product.name,
                'price': str(item.product.price),
            #   'image': str(productDetail.image)  #nếu có hình ảnh thì convert sang string
                'num': 1,
            }
            favourites[item.product.id]=itemFavourite
        request.session['favourites']= favourites
        request.session['quantityfavourite']=quantity
    else:
        favourites.pop(str(favourite_pk))
        request.session['favourites']=favourites
        for key, value in favourites.items():
            quantity += 1
        request.session['quantityfavourite']=quantity
    data = {
            'deleted': True,
            'quantityfavourite':quantity,
        }
    print(request.session['favourites'])
    return JsonResponse(data)