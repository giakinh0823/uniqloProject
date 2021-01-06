from appProduct.views import product
from django.contrib.auth import SESSION_KEY
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import Order, OrderDetail, Cart
from appProduct.models import Product, Gender, Color, ImageProduct, Size, Variants
from django.contrib.auth.decorators import login_required,user_passes_test ,permission_required
from django.template.loader import render_to_string, get_template
from django.views.decorators.csrf import csrf_protect
from register.models import  UserProfile
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
        if productDetail:
            try:
                variant = Variants.objects.get(product= productDetail)
            except Variants.DoesNotExist:
                variant = None
        else:
            variant = None
        if variant:
            colorlist = variant.color.all()
            sizelist = variant.size.all()
            color = colorlist[0]
            size = sizelist[0]
            colorid = Color.objects.filter(name=color)[0].id
            sizeid = Size.objects.filter(name=size)[0].id
        else:
            color = "None+"
            size = "None+"
            sizeid=1010
            colorid=1010
        if request.user.is_authenticated:       
            if id_product in carts.keys():
                itemCart = {
                    'name': productDetail.name,
                    'price': str(productDetail.price),
                    'image': productDetail.image.url,  #nếu có hình ảnh thì convert sang string
                    'num': int(carts[id_product]['num'])+1,
                    'gender': str(productDetail.gender),
                    'color': str(color),
                    'size': str(size),
                    'totalprice':  int((int(carts[id_product]['num'])+1) * int(productDetail.price))
                }
            else:
                itemCart = {
                    'name': productDetail.name,
                    'price': str(productDetail.price),
                    'image': productDetail.image.url,  #nếu có hình ảnh thì convert sang string
                    'num': num,
                    'gender': str(productDetail.gender),
                    'color': str(color),
                    'size': str(size),
                    'totalprice':  int(int(num) * int(productDetail.price))
                }
        else:
            if str(id_product)+str(colorid)+str(sizeid) in carts.keys():
                itemCart = {
                    'name': productDetail.name,
                    'price': str(productDetail.price),
                    'image': productDetail.image.url,  #nếu có hình ảnh thì convert sang string
                    'num': int(carts[str(id_product)+str(colorid)+str(sizeid)]['num'])+1,
                    'gender': str(productDetail.gender),
                    'color': str(color),
                    'size': str(size),
                    'totalprice':  int((int(carts[str(id_product)+str(colorid)+str(sizeid)]['num'])+1) * int(productDetail.price))
                }
            else:
                itemCart = {
                    'name': productDetail.name,
                    'price': str(productDetail.price),
                    'image': productDetail.image.url,  #nếu có hình ảnh thì convert sang string
                    'num': num,
                    'gender': str(productDetail.gender),
                    'color': str(color),
                    'size': str(size),
                    'totalprice':  int(int(num) * int(productDetail.price))
                }
        if request.user.is_authenticated:
            carts[id_product]= itemCart
        else:
            carts[str(id_product)+str(colorid)+str(sizeid)]=itemCart
        request.session['carts'] = carts
        cartInfo = request.session['carts']
        if request.user.is_authenticated:
            try:
                cartItem = Cart.objects.get(product = productDetail,user = request.user, color = itemCart['color'], size = itemCart['size'])
            except Cart.DoesNotExist:
                cartItem = None
            if cartItem != None:
                cartItem.quantity = int(itemCart['num'])
                cartItem.save()
            else:
                newCartItem = Cart(user = request.user, product = productDetail,quantity = int(itemCart['num']), color = itemCart['color'], size = itemCart['size'], image=itemCart['image'])
                newCartItem.save()
            quantity=0
            totalprice=0
            listCart = Cart.objects.filter(user = request.user)
            for item in listCart:
                quantity += int(item.quantity)
                totalprice += int(item.quantity) * int(item.product.price)
            request.session['quantity']=quantity
            print(totalprice)
        else:
            quantity=0
            totalprice=0
            for key, value in cartInfo.items():
                quantity += int(value['num'])
                totalprice += int(value['num'])*int(float(value['price']))
            request.session['quantity']=quantity
        # html = render_to_string('product/addcart.html',{'carts': cartInfo})
    return JsonResponse({'quantity': quantity, 'quantitproduct': itemCart['num'], 'carts': request.session['carts'], 'totalprice': totalprice})

def addcartdetail(request, product_pk):
    if request.is_ajax():
        id_product = request.POST.get('id')
        num = request.POST.get('num')
        colorid = request.POST.get('color')
        sizeid = request.POST.get('size')
        if colorid:
            color = Color.objects.get(id=colorid)
        else: 
            color = "None+"
            colorid=1010
        if sizeid:
            size = Size.objects.get(id=sizeid)
        else:
            size = "None+"
            sizeid=1010
        if num:
            num=num
        else:
            num=1
        productDetail = Product.objects.get(id=id_product)
        if productDetail:
            try:
                variant = Variants.objects.get(product= productDetail)
            except Variants.DoesNotExist:
                variant = None
        else:
            variant = None
        if request.user.is_authenticated:
            if id_product in carts.keys():
                itemCart = {
                    'name': productDetail.name,
                    'price': str(productDetail.price),
                    'image': productDetail.image.url,   #nếu có hình ảnh thì convert sang string
                    'num': int(carts[id_product]['num']) + int(num),
                    'gender': str(productDetail.gender),
                    'color': str(color),
                    'size': str(size),
                    'totalprice':  int(int(num) * int(float(productDetail.price)))
                }
            else:
                itemCart = {
                    'name': productDetail.name,
                    'price': str(productDetail.price),
                    'image': productDetail.image.url,  #nếu có hình ảnh thì convert sang string
                    'num': num,
                    'gender': str(productDetail.gender),
                    'color': str(color),
                    'size': str(size),
                    'totalprice':  int(int(num) * int(float(productDetail.price)))
                }
        else:
            if str(id_product)+str(colorid)+str(sizeid) in carts.keys():
                itemCart = {
                    'name': productDetail.name,
                    'price': str(productDetail.price),
                    'image': productDetail.image.url,   #nếu có hình ảnh thì convert sang string
                    'num': int(carts[str(id_product)+str(colorid)+str(sizeid)]['num']) + int(num),
                    'gender': str(productDetail.gender),
                    'color': str(color),
                    'size': str(size),
                    'totalprice':  int(int(num) * int(float(productDetail.price)))
                }
            else:
                itemCart = {
                    'name': productDetail.name,
                    'price': str(productDetail.price),
                    'image': productDetail.image.url,  #nếu có hình ảnh thì convert sang string
                    'num': num,
                    'gender': str(productDetail.gender),
                    'color': str(color),
                    'size': str(size),
                    'totalprice':  int(int(num) * int(float(productDetail.price)))
                }
        if request.user.is_authenticated:
            carts[id_product]= itemCart
        else:
            carts[str(id_product)+str(colorid)+str(sizeid)]=itemCart
        request.session['carts'] = carts
        cartInfo = request.session['carts']
        if request.user.is_authenticated:
            try:
                cartItem = Cart.objects.get(product = productDetail,user = request.user, color = itemCart['color'], size = itemCart['size'])
            except Cart.DoesNotExist:
                cartItem = None
            if cartItem != None:
                cartItem.quantity = int(itemCart['num'])
                cartItem.totalprice = int(itemCart['num'])*productDetail.price
                cartItem.save()
            else:
                newCartItem = Cart(user = request.user, product = productDetail,quantity = int(itemCart['num']), totalprice = int(itemCart['num'])*productDetail.price, color = itemCart['color'], size = itemCart['size']) 
                newCartItem.save()
            quantity=0
            totalprice=0
            listCart = Cart.objects.filter(user = request.user)
            for item in listCart:
                quantity += int(item.quantity)
                totalprice += int(item.quantity) * int(item.product.price)
            request.session['quantity']=quantity
        else:
            quantity=0
            totalprice=0
            for key, value in cartInfo.items():
                quantity += int(value['num'])
                totalprice += int(value['num'])*int(float(value['price']))
            request.session['quantity']=quantity
        # quantity=0   
        # for key, value in cartInfo.items():
        #     quantity += int(value['num'])  
        # return JsonResponse({'quantity': quantity, 'totalprice': totalprice}) 
    return JsonResponse({'quantity': quantity, 'totalprice': totalprice, 'carts':request.session['carts'] })

def addcartbasket(request):
    if request.is_ajax():
        id_product = request.POST.get('id')
        num = request.POST.get('num')
        color = request.POST.get('color')
        size = request.POST.get('size') 
        name = request.POST.get('name') 
        gender = request.POST.get('gender') 
        price = request.POST.get('price') 
        image = request.POST.get('image') 
        if request.user.is_authenticated:
            pass
        else:
            if color == "None+":
                colorid=1010
            else:
                try:
                    colorid = Color.objects.filter(name=color)[0].id
                except Color.DoesNotExist:
                    colorid=1010
            if size == "None+":
                sizeid=1010
            else:
                try:
                    sizeid = Size.objects.filter(name = size)[0].id
                except Size.DoesNotExist:
                    sizeid=1010
        if request.user.is_authenticated:
            productDetail = Product.objects.get(id=id_product)
            if productDetail:
                try:
                    variant = Variants.objects.get(product= productDetail)
                except Variants.DoesNotExist:
                    variant = None
            else:
                variant = None
            itemCart = {
                'name': productDetail.name,
                'price': str(productDetail.price),
                'image': productDetail.image.url,  #nếu có hình ảnh thì convert sang string
                'num': int(num),
                'gender': str(productDetail.gender),
                'color': color,
                'size': size,
                'totalprice':  int(int(num) * int(float(productDetail.price)))
            }
        else:
            itemCart = {
                'name': name,
                'price': price,
                'image': image,  #nếu có hình ảnh thì convert sang string
                'num': int(num),
                'gender': gender,
                'color': color,
                'size': size,
                'totalprice':  int(int(num) * int(float(price)))
            }
        if request.user.is_authenticated:
            carts[id_product]= itemCart
        else:
            # carts[str(id_product)+str(colorid)+str(sizeid)]=itemCart
            carts[id_product]= itemCart
            print(str(id_product)+str(colorid)+str(sizeid))
        carts[id_product]= itemCart
        request.session['carts'] = carts
        if request.user.is_authenticated:
            try:
               cartItem = Cart.objects.get(product = productDetail,user = request.user, color = itemCart['color'], size = itemCart['size'])
            except Cart.DoesNotExist:
                cartItem = None
            if cartItem != None:
                cartItem.quantity = int(itemCart['num'])
                cartItem.save()
            # else:
            #     newCartItem = Cart(user = request.user, product = productDetail,quantity = int(itemCart['num']), totalprice = int(itemCart['num'])*productDetail.price, color = itemCart['color'], size = itemCart['size']) 
            #     newCartItem.save()
            quantity=0
            totalprice=0
            listCart = Cart.objects.filter(user = request.user)
            for item in listCart:
                quantity += int(item.quantity)
                totalprice += int(item.quantity) * int(item.product.price)
            request.session['quantity']=quantity
        else:
            quantity=0
            totalprice=0   
            for key, value in carts.items():
                quantity += int(value['num'])  
                totalprice += int(value['num']) * int(float(value['price']))    
            request.session['quantity']=quantity
    productprice = int(itemCart['num']) * int(float(itemCart['price']))
    return JsonResponse({'quantity': quantity, 'totalprice': totalprice, 'productprice':productprice, 'carts': request.session['carts']})



def basket(request):
    totalprice = 0;
    quantity = 0;
    if request.user.is_authenticated:
        listCart = Cart.objects.filter(user = request.user)
        for cart in listCart:
            quantity += cart.quantity
            totalprice +=  quantity * cart.product.price
            cart.totalprice= totalprice
            cart.save()
    else:
        listcarts={}
        if  request.session.get('carts'): #kiếm trong trong session có carts không
            listcarts = request.session['carts']
        for key, value in listcarts.items():
            quantity+=int(value['num'])
            totalprice +=  int(value['num']) * int(float(value['price']))
        return render(request, 'order/basket.html', {'listCart': listcarts, 'totalprice': totalprice, 'quantity': quantity} )
    return render(request, 'order/basket.html', {'listCart': listCart, 'totalprice': totalprice, 'quantity': quantity } )

@login_required
def checkout(request):
    cartlist = Cart.objects.filter(user = request.user)
    quantity=0
    totalprice=0
    for cart in cartlist:
        quantity += cart.quantity
        totalprice +=  quantity * cart.product.price
    return render(request,'order/checkout.html', {'cartlist': cartlist, 'quantity': quantity, 'totalprice': totalprice})

def confirmcheckout(request): 
    carts.clear()
    request.session['quantity']=0
    listcarts={}
    totalprice=0
    quantity=0
    if  request.session.get('carts'): #kiếm trong trong session có carts không
        listcarts = request.session['carts']
    listcart = Cart.objects.filter(user = request.user)
    for item in listcart:
        quantity += int(item.quantity)
        totalprice =  item.totalprice
    CODERANDOM = "1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
    code = "";
    while len(code)<8:
        code += random.choice(CODERANDOM)
    order = Order(user = request.user, code = code, totalprice = totalprice, quantity = quantity, address = UserProfile.objects.get(user= request.user).address, phonenumber = UserProfile.objects.get(user= request.user).phonenumber)
    order.save()
    listcart = Cart.objects.filter(user = request.user)
    for item in listcart:
        orderDetail = OrderDetail(order = order, product = Product.objects.get(id=item.product.id),quantity=item.quantity, totalprice = item.totalprice, size=item.size, color = item.color,user = request.user, gender = Product.objects.get(id = item.product.id).gender )
        orderDetail.save()
    Cart.objects.filter(user = request.user).delete()
    try:
        del request.session['carts']
    except KeyError:
        pass
    return  redirect('order:sucesscheckout')


def sucesscheckout(request):
    return render(request, 'order/sucesscheckout.html')



def deletecart(request, cart_pk):
    quantity=0
    totalprice=0
    if request.user.is_authenticated:
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
        cartlist = Cart.objects.filter(user = request.user)
    else:
        try:
            carts.pop(str(cart_pk))
        except:
            pass
        request.session['carts']=carts
        for key, value in carts.items():
            quantity += int(value['num'])
            totalprice +=  int(value['num']) * int(float(value['price']))
        request.session['quantity']=quantity 
        cartlist = carts
    data = {
            'deleted': True,
            'quantity':quantity,
            'totalprice': totalprice,
            'listcart': len(cartlist)
        }
    return JsonResponse(data)