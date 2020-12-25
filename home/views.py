from django.shortcuts import render
from order.models import Cart
from order.views import carts
from appProduct.models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()[0:20]
    if request.user.is_authenticated:
        quantity=0
        carts.clear()
        listCart = Cart.objects.filter(user = request.user)
        for item in listCart:
            quantity += int(item.quantity)
            itemCart = {
                'name': item.product.name,
                'price': str(item.product.price),
            #   'image': str(productDetail.image)  #nếu có hình ảnh thì convert sang string
                'num': item.quantity,
            }
            carts[item.product.id]=itemCart
        request.session['quantity']=quantity
        request.session['carts']=carts
        return render(request, 'home/index.html', {'quantity': quantity, 'products': products})
    else:
        return render(request, 'home/index.html',{'products': products})
