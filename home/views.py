from django.shortcuts import render
from order.models import Cart
from order.views import carts

# Create your views here.


def index(request):
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
        return render(request, 'home/index.html', {'quantity': quantity})
    else:
        return render(request, 'home/index.html')
