from typing import cast
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render, redirect,get_object_or_404, render_to_response
from .models import Product, Category
from .forms import ProductForm, VariantsForm 
from django.contrib.auth.decorators import login_required,user_passes_test ,permission_required
from django.template.loader import render_to_string, get_template
from django.views.decorators.csrf import csrf_protect
from order.models import Order, Cart
from django.db.models import Q
from .filters import ProductFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import random


# Create your views here.


def product(request):
    # products = Product.objects.all()
    product_list = Product.objects.all()

    categorys = Category.objects.all()
    
    page = request.GET.get('page', 1)
    paginator = Paginator(product_list, 12)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    if request.GET:
        productFilter = ProductFilter(request.GET, queryset= product_list)
        product_list = productFilter.qs

        page = request.GET.get('page',1)
        paginator = Paginator(product_list, 12)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
            
        return render(request, 'product/product.html', {'products': products, 'productFilter': productFilter, 'categorys': categorys})
    return render(request, 'product/product.html', {'products': products, 'categorys': categorys})

#search_ajax
def searchProduct(request):
    if request.method == "GET":
        search_text = request.GET['search_text']
        if search_text is not None and search_text != u"":
            search_text = request.GET['search_text']
    else:
        search_text = ''
    product_list = Product.objects.filter(name__contains = search_text)
    
    page = request.GET.get('page', 1)
    paginator = Paginator(product_list, 12)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'product/ajax_search.html', {'products':products})
    

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
    return render(request, 'product/createproduct.html', {'form': ProductForm(), 'categorys': categorys, 'variantsForm': VariantsForm()})

@login_required
def editproduct(request , product_pk):
    product = get_object_or_404(Product, pk=product_pk, user= request.user)
    # if request.method == "GET": 
    #     form = ProductForm(instance=product)
    #     categorys = Category.objects.all()
    #     return render(request, 'product/editproduct.html', {'product' : product , 'form': form, 'categorys': categorys})
    # else:
    #     category = str(request.POST['category'])
    #     product.category = Category.objects.filter(name = category)[0]
    #     if 'image' in request.FILES:
    #         product.image = request.FILES['image']
    #     product.save()
    #     form = ProductForm(request.POST, instance = product)
    #     form.save()
    #     return redirect('appProduct:productuser')
    
    # ajax edit 
    form = ProductForm(instance=product)
    categorys = Category.objects.all()
    if request.is_ajax():
        category = str(request.POST['category'])
        product.category = Category.objects.filter(name = category)[0]
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        form = ProductForm(request.POST, instance = product)
        form.save()
        return JsonResponse({'response': "Success"})
    else:
        return render(request, 'product/editproduct.html', {'product' : product , 'form': form, 'categorys': categorys})


@login_required
def deleteproduct(request, product_pk):
    # product = get_object_or_404(Product, pk=product_pk, user=request.user) #lấy thông tin todo nếu ko có trả về 404
    # if request.method == "POST": 
    #     product.delete()
    #     return redirect('appProduct:productuser')
    
    #ở đây dùng ajax
    product = get_object_or_404(Product, pk=product_pk, user=request.user)
    product.delete()
    data = {
            'deleted': True
        }
    return JsonResponse(data)

def detailproduct(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    return render(request, 'product/detailproduct.html', {'product': product})




