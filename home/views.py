from django.shortcuts import render
from order.models import Cart
from order.views import carts
from favourite.views import favourites
from appProduct.models import Product, Category, Gender, Variants
from favourite.models import Favourite

# Create your views here.

def index(request):
    products = Product.objects.all()[0:20]
    categorys = Category.objects.all()
    genders = Gender.objects.all()
    variants = Variants.objects.all()
    if request.user.is_authenticated:
        favourites.clear()
        carts.clear()
        listCart = Cart.objects.filter(user = request.user)
        listfavourite = Favourite.objects.filter(user = request.user)
        quantity=0
        quantityfavourite=0
        for item in listCart:
            quantity += int(item.quantity)
            itemCart = {
                'name': item.product.name,
                'price': str(item.product.price),
            #   'image': str(productDetail.image)  #nếu có hình ảnh thì convert sang string
                'num': item.quantity,
            }
            carts[item.product.id]=itemCart

        for item in listfavourite:
            quantityfavourite+=1
            itemFavourite = {
                'name': item.product.name,
                'price': str(item.product.price),
                #'image': str(productDetail.image)  #nếu có hình ảnh thì convert sang string
            }
            favourites[item.product.id]=itemFavourite
        request.session['quantityfavourite'] = quantityfavourite
        request.session['favourites'] = favourites
        request.session['quantity']=quantity
        request.session['carts']=carts
        return render(request, 'home/index.html', {'quantity': quantity, 'products': products, 'variants': variants})
    else:
        return render(request, 'home/index.html',{'products': products, 'variants': variants})
