from django.contrib.auth import SESSION_KEY
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render, redirect,get_object_or_404, render_to_response
from .models import Order, OrderDetail, Cart
from appProduct.models import Product
from django.contrib.auth.decorators import login_required,user_passes_test ,permission_required
from django.template.loader import render_to_string, get_template
from django.views.decorators.csrf import csrf_protect
import random
# Create your views here.

# for key, value in request.session.carts.items
#     key: value


carts = {}
def addcart(request):
    if request.is_ajax():
        id_product = request.POST.get('id')
        num = request.POST.get('num')
        productDetail = Product.objects.get(id=id_product)
        if id_product in carts.keys():
            itemCart = {
                'name': productDetail.name,
                'price': str(productDetail.price),
            #   'image': str(productDetail.image)  #nếu có hình ảnh thì convert sang string
                'num': int(carts[id_product]['num'])+1,
            }
        else:
            itemCart = {
                'name': productDetail.name,
                'price': str(productDetail.price),
            #   'image': str(productDetail.image)  #nếu có hình ảnh thì convert sang string
                'num': num,
            }
        carts[id_product]= itemCart
        request.session['carts'] = carts
        cartInfo = request.session['carts']
        if request.user.is_authenticated:
            try:
                cartItem = Cart.objects.get(product = productDetail,user = request.user)
            except Cart.DoesNotExist:
                cartItem = None
            if cartItem != None:
                cartItem.quantity = int(itemCart['num'])
                cartItem.save()
            else:
                newCartItem = Cart(user = request.user, product = productDetail,quantity = int(itemCart['num'])) 
                newCartItem.save()
            quantity=0
            listCart = Cart.objects.filter(user = request.user)
            for item in listCart:
                quantity += int(item.quantity)
            request.session['quantity']=quantity
        else:
            quantity=0
            for key, value in cartInfo.items():
                quantity += int(value['num'])
                request.session['quantity']=quantity
        # html = render_to_string('product/addcart.html',{'carts': cartInfo})
    return JsonResponse({'quantity': quantity})

def addcartdetail(request, product_pk):
    if request.is_ajax():
        id_product = request.POST.get('id')
        num = request.POST.get('num')
        if num:
            num=num
        else:
            num=1
        productDetail = Product.objects.get(id=id_product)
        if id_product in carts.keys():
            itemCart = {
                'name': productDetail.name,
                'price': str(productDetail.price),
            #   'image': str(productDetail.image)  #nếu có hình ảnh thì convert sang string
                'num': int(carts[id_product]['num']) + int(num),
            }
        else:
            itemCart = {
                'name': productDetail.name,
                'price': str(productDetail.price),
            #   'image': str(productDetail.image)  #nếu có hình ảnh thì convert sang string
                'num': num,
            }
        carts[id_product]= itemCart
        request.session['carts'] = carts
        cartInfo = request.session['carts']
        if request.user.is_authenticated:
            try:
                cartItem = Cart.objects.get(product = productDetail,user = request.user)
            except Cart.DoesNotExist:
                cartItem = None
            if cartItem != None:
                cartItem.quantity = int(itemCart['num'])
                cartItem.save()
            else:
                newCartItem = Cart(user = request.user, product = productDetail,quantity = int(itemCart['num'])) 
                newCartItem.save()
            quantity=0
            listCart = Cart.objects.filter(user = request.user)
            for item in listCart:
                quantity += int(item.quantity)
            request.session['quantity']=quantity
        else:
            quantity=0
            for key, value in cartInfo.items():
                quantity += int(value['num'])
                request.session['quantity']=quantity
        # quantity=0   
        # for key, value in cartInfo.items():
        #     quantity += int(value['num'])  
    return JsonResponse({'quantity': quantity})

def addcartbasket(request):
    if request.is_ajax():
        id_product = request.POST.get('id')
        num = request.POST.get('num')
        productDetail = Product.objects.get(id=id_product)
        itemCart = {
            'name': productDetail.name,
            'price': str(productDetail.price),
            # 'image': str(productDetail.image)  #nếu có hình ảnh thì convert sang string
            'num': num,
        }
        carts[id_product]= itemCart
        request.session['carts'] = carts
        if request.user.is_authenticated:
            try:
                cartItem = Cart.objects.get(product = productDetail,user = request.user)
            except Cart.DoesNotExist:
                cartItem = None
            if cartItem != None:
                cartItem.quantity = int(itemCart['num'])
                cartItem.save()
            else:
                newCartItem = Cart(user = request.user, product = productDetail,quantity = int(itemCart['num'])) 
                newCartItem.save()
            quantity=0
            listCart = Cart.objects.filter(user = request.user)
            for item in listCart:
                quantity += int(item.quantity)
            request.session['quantity']=quantity
        # quantity=0   
        # for key, value in cartInfo.items():
        #     quantity += int(value['num'])  
    return JsonResponse({'quantity': quantity})



def basket(request):
    totalprice = 0;
    quantity = 0;
    if request.user.is_authenticated:
        listCart = Cart.objects.filter(user = request.user)
        for cart in listCart:
            quantity += cart.quantity
            totalprice +=  quantity * cart.product.price
    else:
        listcarts={}
        if  request.session.get('carts'): #kiếm trong trong session có carts không
            listcarts = request.session['carts']
        for key, value in listcarts.items():
            quantity+=int(value['num'])
            totalprice +=  int(value['num']) * int(float(value['price']))
        return render(request, 'order/basket.html', {'listCart': listcarts, 'totalprice': totalprice} )
    return render(request, 'order/basket.html', {'listCart': listCart, 'totalprice': totalprice , 'data': [1,2,3,4,5,6,7,8,9,10]} )

@login_required
def checkout(request):
    return render(request,'order/checkout.html')

def confirmcheckout(request): 
    carts.clear()
    Cart.objects.filter(user = request.user).delete()
    request.session['quantity']=0
    listcarts={}
    totalprice=0
    quantity=0
    if  request.session.get('carts'): #kiếm trong trong session có carts không
        listcarts = request.session['carts']
    for key, value in listcarts.items():
        quantity += int(value['num'])
        totalprice +=  int(value['num']) * int(float(value['price']))
    CODERANDOM = "1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
    code = "";
    for i in range(8):
        code += random.choice(CODERANDOM)
    order = Order(user = request.user, state = "Waiting",code = code, totalprice = totalprice, quantity = quantity)
    order.save()
    for key, value in listcarts.items():
        orderDetail = OrderDetail(order = order, product = Product.objects.get(id=key),quantity=int(value['num']), totalprice = int(value['num']) * int(float(value['price'])))
        orderDetail.save()
    try:
        del request.session['carts']
    except KeyError:
        pass
    return  redirect('home:index')



def deletecart(request, cart_pk):
    quantity=0
    totalprice=0
    if request.user.is_authenticated:
        print(request.session['carts'])
        cart = get_object_or_404(Cart, pk=cart_pk, user = request.user)
        cart.delete()
        cartlist = Cart.objects.filter(user = request.user)
        carts.clear()
        for item in cartlist:
            quantity += int(item.quantity)
            totalprice +=  quantity * item.product.price
            itemCart = {
                'name': item.product.name,
                'price': str(item.product.price),
            #   'image': str(productDetail.image)  #nếu có hình ảnh thì convert sang string
                'num': item.quantity,
            }
            carts[item.product.id]=itemCart
        request.session['carts']= carts
        request.session['quantity']=quantity
    #     cartlist = Cart.objects.filter(user = request.user)
    #     for cart in cartlist:
    #         quantity += cart.quantity
    #         totalprice +=  quantity * cart.product.price
    #     request.session['quantity']=quantity
    else:
        carts.pop(str(cart_pk))
        request.session['carts']=carts
        for key, value in carts.items():
            quantity += int(value['num'])
            totalprice +=  int(value['num']) * int(float(value['price']))
        request.session['quantity']=quantity
    data = {
            'deleted': True,
            'quantity':quantity,
            'totalprice': totalprice
        }
    return JsonResponse(data)