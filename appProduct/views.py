from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render, redirect,get_object_or_404, render_to_response
from .models import Order, OrderDetail, Product
from .forms import ProductForm, Category
from django.contrib.auth.decorators import login_required,user_passes_test ,permission_required
from django.template.loader import render_to_string, get_template
from django.views.decorators.csrf import csrf_protect
import random


# Create your views here.


def product(request):
    products = Product.objects.all()
    return render(request, 'product/product.html', {'products': products})

@login_required
def productuser(request):
    products = Product.objects.filter(user = request.user)
    return render(request, 'product/productuser.html', {'products': products})

@login_required
def createproduct(request):
    #ở đây không dùng ajax
    # if request.method == "GET": 
    #     categorys = Category.objects.all()
    #     return render(request, 'product/createproduct.html', {'form': ProductForm(), 'categorys': categorys})
    # else:
    #     form = ProductForm(request.POST)
    #     product = form.save(commit=False)
    #     product.user = request.user
    #     category = str(request.POST['category'])
    #     product.category = Category.objects.filter(name = category)[0]
    #     product.save()
    #     return redirect('appProduct:productuser')
    #ở đây dùng ajax
    categorys = Category.objects.all()
    if request.is_ajax(): #nếu như yêu cầu nhận được là ajax
        categorys = Category.objects.all()
        form = ProductForm(request.POST)
        product = form.save(commit=False)
        product.user = request.user
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        category = str(request.POST['category'])
        product.category = Category.objects.filter(name = category)[0]
        product.save()
        return JsonResponse({'response':"Success"})
    return render(request, 'product/createproduct.html', {'form': ProductForm(), 'categorys': categorys})

@login_required
def editproduct(request , product_pk):
    product = get_object_or_404(Product, pk=product_pk, user= request.user)
    if request.method == "GET": 
        form = ProductForm(instance=product)
        categorys = Category.objects.all()
        return render(request, 'product/editproduct.html', {'product' : product , 'form': form, 'categorys': categorys})
    else:
        category = str(request.POST['category'])
        product.category = Category.objects.filter(name = category)[0]
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        form = ProductForm(request.POST, instance = product)
        form.save()
        return redirect('appProduct:productuser')
    
    #ajax edit 
    # form = ProductForm(instance=product)
    # categorys = Category.objects.all()
    # if request.is_ajax():
    #     category = str(request.POST['category'])
    #     product.category = Category.objects.filter(name = category)[0]
    #     if 'image' in request.FILES:
    #         product.image = request.FILES['image']
    #     product.save()
    #     form = ProductForm(request.POST, instance = product)
    #     form.save()
    #     return JsonResponse({'response':"Success"})
    # return render(request, 'product/editproduct.html', {'product' : product , 'form': form, 'categorys': categorys})


@login_required
def deleteproduct(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk, user=request.user) #lấy thông tin todo nếu ko có trả về 404
    if request.method == "POST": 
        product.delete()
        return redirect('appProduct:productuser')

def detailproduct(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    return render(request, 'product/detailproduct.html', {'product': product})


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
        quantity=0
        for key, value in cartInfo.items():
            quantity += int(value['num'])
        request.session['quantity'] = quantity
        # html = render_to_string('product/addcart.html',{'carts': cartInfo})
    return JsonResponse({'quantity':quantity})

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
        quantity=0
        for key, value in cartInfo.items():
            quantity += int(value['num'])
    return JsonResponse({'quantity':quantity})


def basket(request):
    totalprice = 0;
    listcarts={}
    if  request.session.get('carts'): #kiếm trong trong session có carts không
        listcarts = request.session['carts']
    for key, value in listcarts.items():
        totalprice +=  int(value['num']) * int(float(value['price']))
    return render(request, 'product/basket.html', {'carts': listcarts, 'totalprice': totalprice} )

@login_required
def checkout(request):
    return render(request,'product/checkout.html')

def confirmcheckout(request):
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
    for i in range(10):
        code += random.choice(CODERANDOM)
    order = Order(user = request.user, state = "Waiting",code = code, totalprice = totalprice, quantity = quantity)
    order.save()
    for key, value in listcarts.items():
        orderDetail = OrderDetail(order = order, product = Product.objects.get(id=key),quantity=int(value['num']), totalprice = int(value['num']) * int(float(value['price'])))
        orderDetail.save()
    return  redirect('home:index')
       

